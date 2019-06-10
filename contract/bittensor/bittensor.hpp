/**
 *  @file
 *  @copyright defined in eos/LICENSE.txt
 */
#pragma once

#include <eosiolib/asset.hpp>
#include <eosiolib/eosio.hpp>
#include <string>

namespace eosiosystem {
   class system_contract;
}

namespace eosio {

   using std::string;

   class [[eosio::contract("bittensor")]] bittensor : public contract {
      public:
         using contract::contract;

         bittensor(name receiver, name code, datastream<const char*> ds):contract(receiver, code, ds) {}

         [[eosio::action]]
         void upsert( name user,
                      std::string address,
                      std::string port );

         [[eosio::action]]
         void erase( name user );

         [[eosio::action]]
         void grade( name  user,
                     const std::vector<name>& edges,
                     const std::vector<float>& attribution );

         [[eosio::action]]
         void create( name   issuer,
                      asset  maximum_supply );

         [[eosio::action]]
         void issue( name to, asset quantity, string memo );

         [[eosio::action]]
         void retire( asset quantity, string memo );

         [[eosio::action]]
         void transfer( name    from,
                        name    to,
                        asset   quantity,
                        string  memo );

         [[eosio::action]]
         void open( name owner, const symbol& symbol, name ram_payer );

         [[eosio::action]]
         void close( name owner, const symbol& symbol );

         static asset get_supply( name token_contract_account, symbol_code sym_code )
         {
            stats statstable( token_contract_account, sym_code.raw() );
            const auto& st = statstable.get( sym_code.raw() );
            return st.supply;
         }

         static asset get_balance( name token_contract_account, name owner, symbol_code sym_code )
         {
            accounts accountstable( token_contract_account, owner.value );
            const auto& ac = accountstable.get( sym_code.raw() );
            return ac.balance;
         }

         using upsert_action = eosio::action_wrapper<"upsert"_n, &bittensor::upsert>;
         using grade_action = eosio::action_wrapper<"grade"_n, &bittensor::grade>;
         using erase_action = eosio::action_wrapper<"erase"_n, &bittensor::erase>;
         using create_action = eosio::action_wrapper<"create"_n, &bittensor::create>;
         using issue_action = eosio::action_wrapper<"issue"_n, &bittensor::issue>;
         using retire_action = eosio::action_wrapper<"retire"_n, &bittensor::retire>;
         using transfer_action = eosio::action_wrapper<"transfer"_n, &bittensor::transfer>;
         using open_action = eosio::action_wrapper<"open"_n, &bittensor::open>;
         using close_action = eosio::action_wrapper<"close"_n, &bittensor::close>;

      private:

        struct [[eosio::table]] peer {
          name identity;
          std::string address;
          std::string port;
          std::vector<name> edges;
          std::vector<float> attribution;
          uint64_t primary_key() const { return identity.value;}
        };

        struct [[eosio::table]] account {
          asset    balance;

          uint64_t primary_key()const { return balance.symbol.code().raw(); }
        };

        struct [[eosio::table]] currency_stats {
          asset    supply;
          asset    max_supply;
          name     issuer;

          uint64_t primary_key()const { return supply.symbol.code().raw(); }
        };

        typedef eosio::multi_index<"peers"_n, peer> peer_table;
        typedef eosio::multi_index< "accounts"_n, account > accounts;
        typedef eosio::multi_index< "stat"_n, currency_stats > stats;

        void sub_balance( name owner, asset value );
        void add_balance( name owner, asset value, name ram_payer );
   };

} /// namespace eosio
