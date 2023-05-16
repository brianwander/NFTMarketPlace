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
    contract_address=st.sidebar.text_input("NFT collection contract address")


#In the Mint tab:
with tab2:
    st.warning("By using this service you agree that the work you are uploading is your own, original artwork.",icon="⛔️")#Displays a warning message to the user
    artwork=st.file_uploader("Upload your artwork here for minting") #Allows users to upload a file
    if st.button("Display Artwork"): #A button that displays the uploaded image
        st.image(artwork)
    address=st.text_input("Address to which the NFT will be minted") #The address that will own the NFT
    nft_name=st.text_input("Give a name to your NFT")
    nft_description=st.text_input("Price your NFT in MATIC")
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
    if st.button("View NFT"):#Allow users view artwork given the token ID
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk=ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(str(contract_address))
        output=contract.get(token_id)
        st.write("Name:",output.metadata.name)
        st.image(output.metadata.image)
        st.write("Price in MATIC:",output.metadata.description)
        st.write("Owner:",output.owner)

#In the Trade tab:
with tab4:
    receiver_address=st.text_input("Wallet address to receive an NFT")
    token_id=st.text_input("Token ID")
    if st.button("Preview NFT"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk=ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(str(contract_address))
        output=contract.get(token_id)
        st.write("Name:",output.metadata.name)
        st.image(output.metadata.image)
        st.write("Price in MATIC:",output.metadata.description)
        st.write("Current owner",output.owner)
    st.write("Transfer an NFT after you have received sufficient MATIC")
    if st.button("Transfer NFT"):
        load_dotenv()
        private_key=os.getenv("mumbai_private_key")
        sdk=ThirdwebSDK.from_private_key(private_key,"mumbai")
        contract=sdk.get_nft_collection(contract_address)
        st.write(contract.transfer(receiver_address,token_id))
    
    #listing_number=st.text_input("Listing ID")
    #receiver=st.text_input("Receiver for the NFT")
    #if st.button("Buy NFT"):
    #    load_dotenv()
    #    private_key=os.getenv("mumbai_private_key")
    #    sdk=ThirdwebSDK.from_private_key(private_key,"mumbai")
    #    contract=sdk.get_marketplace(marketplace_contract_address)
    #    st.write(contract.buyout_listing(listing_id=listing_number,quantity_desired=1,receiver=receiver))
    #recipient_address=st.text_input("Recipient Address") #The address of the recipient of the transaction
    #sender_address=st.text_input("Your Address") #Transaction sender
    #nft_address=st.text_input("NFT Address") #NFT to transact
    #st.write("Buy")