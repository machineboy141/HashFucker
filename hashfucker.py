import itertools
import hashlib
import string


__author__ = "Ömer Hasan Durmuş"


def cevir(chars,length):
    for cevirilmis in itertools.product(chars,repeat=length):
        yield "".join(cevirilmis)


def hashver(hashword,i,md5):

    hashq = bytes(hashword,"utf-8")
    hash = hashlib.md5(hashq).hexdigest()

    
    print(i,"> ",hash,"==",hashword)

    if md5 == hash:
        print("HASH CRACKED ! >>>>>>>",hashword)
        exit(0)
    
def main():

    md5 = input("MD5:")

    i = 1
    text = string.ascii_letters + string.digits + string.punctuation

    for textlen in range(1,20):
        
        for word in cevir(text,textlen):
            hashver(word,i,md5)
            
            i += 1


if __name__ == "__main__":

    main()

