# NFTMarketPlace
Mint NFTs from your own original artwork, browse NFTs minted by various users, and easily trade them using this NFT Marketplace application!

## Installations:
We recommend creating a new conda environment using python 3.9.16 to contain all of the installation as it may not work with an earlier version of python.

To create a new conda environment, type the following command into your terminal application:<br>
'conda create -n NFTMarketplace python=3.9'

The installations necessary to run this application are as follows:<br>
Install python-dotenv by typing the following command into your terminal application:<br>
'pip install python-dotenv'<br>
Install streamlit by typing the following command into your terminal application:<br>
'pip install streamlit'<br>
Install thirdweb sdk by typing the following command into your terminal application:<br>
'pip install thirdweb-sdk'<br>

## Other important setup steps:
1.Metamask must be installed to access the network that will host the contract. Go to https://metamask.io/download/ and follow the steps to add metamask to your browser. You must create an account to use this application.<br>

2.Add the Mumbai Network to your metamask wallet. To do this, go to https://mumbai.polygonscan.com/ and click "Add Mumbai Network." Follow the instructions on the Metamask browser extension to connect your wallet to the Mumbai network.<br>

3.Once your account is made and connected to the mumbai network, you must save your private key to a .env file saved on the same directory as the streamlit_app.py file. To obtain the private key from your Mumbai Network account open metamask, click the three dots and then click account details. Click export private key, then type your password to obtain the private key. Save your key to the .env file in the following format:<br>

'mumbai_private_key= '************************' '

4.Connect your wallet to thirdweb. Go to https://thirdweb.com/dashboard/contracts and connect your metamask wallet. Click ready-to-deploy, then select NFT collection. Click the Deploy now button. Give a name to the contract, and paste your wallet address from metamask into all of the address boxes. In the Network/Chain section, select the Mumbai network, and connect using Metamask. Press the deploy now button, then follow the steps to receive MATIC from the faucet for testing. Deploy the contract.<br>

5.Navigate to the contracts screen on the thirdweb site at https://thirdweb.com/dashboard/contracts. Note the contract address for later use in the application.<br>

## Imports: 
The following libraries are used in this NFT Marketplace program:<br>
Dotenv is used to load the private key saved in the .env file.<br>
Thirdweb is used to interact with the contract using python. Minting, browsing and transferring NFTs are all done through the thirdweb library.<br>
Streamlit was used to create the web interface of the application.<br>

## Usage:
Navigate to the folder containing the streamlit_app.py file and type <br>
'streamlit run streamlit_app.py'<br>

Paste the contract address into the box in the sidebar. <br>

Navigate to the mint tab to mint an NFT. Upload an artwork as an image file under 200MB using the Browse files button. The display artwork button will show the image you have uploaded on the web interface. Paste the address to which you want to mint the NFT. Give it a name and a price in MATIC, then click the Mint NFT button to mint the NFT. The receipt will appear, as well as the token id and blockchain information. At this point, you can also view the NFT on the thirdweb site, along with its token id and price.<br>

Click the browse tab to browse NFTs on the contract. Click 'Load my balance' to see how many NFTs you own. You can also view other user's NFT balance by typing their address. If you know the token ID for an NFT you are interested in, type it into the corresponding box and click "View NFT." This will show the NFT's name, price, and owner as well as an image of the NFT.<br>

The trade tab allows users to transfer NFTs from the connected wallet to any other wallet address. Type the wallet address to which you want to send an NFT to, and the token ID corresponding to the NFT you would like to send. You can preview the NFT by clicking the Preview NFT button to ensure you are sending the correct token. Clicking the Transfer NFT button will transfer ownership of your NFT to the selected address- Make sure you have received your payment on Metamask before using this function.<br>

## License

Apache License

## Contributors
By Brian Wander <br>
Email brianwander101@gmail.com <br>
Linkedin https://www.linkedin.com/in/brian-wander-514326258/
