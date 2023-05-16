from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv
import os

#Loading env keys
load_dotenv()

#Private key from .env file
private_key=os.getenv("mumbai_private_key")

def mint_nft(contract_object,name,description,image,address):
    if isinstance(image,str):
        metadata=NFTMetadataInput.from_json({
            "name":str(name),
            "description":description,
            "image":open(str(image),"rb")
        })
    else:
        metadata=NFTMetadataInput.from_json({
            "name":str(name),
            "description":description,
            "image":image
        })

    tx=contract_object.mint_to(address,metadata)
    receipt=tx.receipt
    token_id=tx.id
    nft=tx.data()
    return (receipt,token_id,nft)

#Instancing the sdk connecting to the Mumbai test network
#sdk= ThirdwebSDK.from_private_key(private_key,"mumbai")
#Connecting to the contract using the contract address
#contract = sdk.get_nft_collection("0x297ac046023cA74Af33007af2a6bf4cBD1a56540")
#
#metadata=NFTMetadataInput.from_json({
#    "name":"Testing_NFT",
#    "description":"This is a testing NFT",
#    "image":open("me2.PNG","rb")
#})
#tx=contract.mint(metadata)
#receipt=tx.receipt
#token_id=tx.id
#nft=tx.data()

