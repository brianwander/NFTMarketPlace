import streamlit as st
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv
import os
from functions import mint_nft

#Names for the different tabs of the streamlit application
tab1,tab2,tab3,tab4 = st.tabs(["Welcome","Mint","Browse","Trade"])
#In the Welcome tab:
with tab1:
    st.title("NFT Marketplace")#Title
    st.header("Mint NFTs from your original artwork, and buy and sell them on the Ethereum Blockchain")#Explanation of the application
    st.write("First, input the contract address below. Then, head over to the Mint tab to upload your work, or the Trade screen to buy and sell NFTs")#How to use the application
    contract_address=st.sidebar.text_input("NFT Contract address")


#In the Mint tab:
with tab2:
    st.warning("By using this service you agree that the work you are uploading is your own, original artwork.",icon="⛔️")#Displays a warning message to the user
    artwork=st.file_uploader("Upload your artwork here for minting") #Allows users to upload a file
    if st.button("Display Artwork"): #A button that displays the uploaded image
        st.image(artwork)
    address=st.text_input("Address to which the NFT will be minted") #The address that will own the NFT
    nft_name=st.text_input("Give a name to your NFT")
    nft_description=st.text_input("Give a description to your NFT")
    if st.button("Mint NFT"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk= ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract = sdk.get_nft_collection(str(contract_address))
        receipt,token_id,nft=mint_nft(contract_object=contract,name=nft_name,description=nft_description,image=artwork,address=address)
        st.write("Receipt",receipt)
        st.write("Token ID",token_id)
        st.write("NFT",nft)
#contract.call("function_name", "arg1", "arg2") #Pseudocode for functions
#contract.call("mintto",artwork) #Pseudocode for minting

#In the Browse tab:
with tab3:
    if st.button("Load my Balance"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk= ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(str(contract_address))
        st.write(contract.balance())
    st.write("Show another address' balance")
    view_balance_address=st.text_input("Wallet address to view NFT balance")
    if st.button("Load wallet's balance"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk= ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(str(contract_address))
        st.write(contract.balance_of(view_balance_address))
    token_id=st.text_input("NFT ID to view") #User input of the artwork address
    if st.button("View NFT"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk=ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(str(contract_address))
        output=contract.get(token_id)
        st.write("Name:",output.metadata.name)
        st.image(output.metadata.image)
        st.write("Description:",output.metadata.description)
        st.write("Owner:",output.owner)
    #Allow users view artwork
    st.text_input("Wallet address")
    #Allow users to view held NFTs and transactions associated with a given address.
    st.write("Blockchain history")
    #Allows users to view the history of transactions on the blockchain.

#In the Trade tab:
with tab4:
    recipient_address=st.text_input("Recipient Address") #The address of the recipient of the transaction
    sender_address=st.text_input("Your Address") #Transaction sender
    nft_address=st.text_input("NFT Address") #NFT to transact
    #contract.call("TransactionMethod")