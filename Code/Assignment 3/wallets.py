l=list(map(int,input().split(' ')))
print("The fattest wallet has ${0} in it".format(max(l)))
print("The skinniest wallet has ${0} in it".format(min(l)))
print("All together, these wallets have ${0} in them".format(sum(l)))
print("All together, the total value of these wallets is worth ${0} dimes.".format(sum(l)*10))

