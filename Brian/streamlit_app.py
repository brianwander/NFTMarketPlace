import streamlit as st
from thirdweb import ThirdwebSDK

tab1,tab2,tab3,tab4 = st.tabs(["Welcome","Mint","Browse","Trade"])

with tab1:
    st.title("NFT Marketplace")
    st.header("Mint NFTs from your original artwork, and buy and sell them on the Ethereum Blockchain")
    st.write("Head over to the Mint tab to upload your work, or the Trade screen to buy and sell NFTs")

with tab2:
    artwork=st.file_uploader("Upload your artwork here for minting")
    if st.button("Display Artwork"):
        st.image(artwork)
    address=st.text_input("Address to which the NFT will be minted")
#contract.call("function_name", "arg1", "arg2")
#contract.call("mintto",artwork)

with tab3:
    st.text_input("Artwork address")
    #Allow users view artwork
    st.text_input("Wallet address")
    #Allow users to view held NFTs and transactions associated with a given address.
    st.write("Blockchain history")
    #Allows users to view the history of transactions on the blockchain.

with tab4:
    recipient_address=st.text_input("Recipient Address")
    sender_address=st.text_input("Your Address")
    nft_address=st.text_input("NFT Address")
    #contract.call("TransactionMethod")