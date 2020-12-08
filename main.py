#cosists blocks
# blocks consit transaction
#blocks are connect trought hashing
#transaction+ previous block fingerprint


from Block import Block
blockchains = []

genesis_block = Block("chancellor of the brink...", ["sat6oshi sent 1 Btc to Ivan",
"maria sent 5 Btc to jenny",
"satoshi sent 5 btc to Hal"])


second_block = Block(genesis_block.block_hash, ["ivan sent 5 btc to l"])
third_block = Block(second_block.block_hash, ["ivan sent t6o bb 5tbc"])


print("block hash:second block:")
print(genesis_block.block_hash)

print("block hash:second block")
print(second_block.block_hash)

print("block hash:third block")
print(third_block.block_hash)

