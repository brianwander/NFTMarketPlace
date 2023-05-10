import streamlit as st
from thirdweb import ThirdwebSDK

#Names for the different tabs of the streamlit application
tab1,tab2,tab3,tab4 = st.tabs(["Welcome","Mint","Browse","Trade"])
#In the Welcome tab:
with tab1:
    st.title("NFT Marketplace")#Title
    st.header("Mint NFTs from your original artwork, and buy and sell them on the Ethereum Blockchain")#Explanation of the application
    st.write("Head over to the Mint tab to upload your work, or the Trade screen to buy and sell NFTs")#How to use the application
#In the Mint tab:
with tab2:
    st.warning("By using this service you agree that the work you are uploading is your own, original artwork.",icon="⛔️")#Displays a warning message to the user
    artwork=st.file_uploader("Upload your artwork here for minting") #Allows users to upload a file
    if st.button("Display Artwork"): #A button that displays the uploaded image
        st.image(artwork)
    address=st.text_input("Address to which the NFT will be minted") #The address that will own the NFT
#contract.call("function_name", "arg1", "arg2") #Pseudocode for functions
#contract.call("mintto",artwork) #Pseudocode for minting

#In the Browse tab:
with tab3:
    st.text_input("Artwork address") #User input of the artwork address
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