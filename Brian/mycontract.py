from thirdweb import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
from web3 import Account
from web3 import middleware
from thirdweb.types.settings.metadata import NFTCollectionContractMetadata
from bip44 import Wallet
import os

def generate_account():
    #Access the mnemonic phrase from the .env file
    mnemonic=os.getenv("MNEMONIC")
    #Create wallet object
    wallet= Wallet(mnemonic)
    #Derive account keys
    private,public= wallet.derive_account("eth")
    #Convert the private key into an ethereum account
    account= Account.privateKeyToAccount(private)
    #Return the account from the function
    return account
#Generating the account to sign transactions
account=generate_account()

#Setting the URL to the Ganache blockchain to connect to it later
RPC_URL= "HTTP://127.0.0.1:7545"

#Setting the provider to pass into the SDK
provider=Web3(Web3.HTTPProvider(RPC_URL))

#Creating an instance of the SDK to use
sdk = ThirdWebSDK(provider,account)

sdk.deployer.deploy_nft_collection(NFTCollectionContractMetadata(name="My Python SmartContract"))