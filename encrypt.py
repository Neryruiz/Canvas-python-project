#nery ruiz
#RSA encryption for password
import math
import random
import sys
import threading
from queue import Queue


print("Using RSA encryption")
class encrypt():
    def __init__(self):
        self.character = {}
        
        #print(self.character)

        prime = self.prime_gen(100, 10000) #gen list of primes
        #prime_size = len(prime)
        self.prime_q = 23#3833#prime[random.randint(prime_size//2, prime_size-1)]#q
        self.prime_p = 7#3127#prime[random.randint(0, (prime_size//2)-1)]#p
        #print(self.prime_q)
        #print(self.prime_p)

        self.modulus_n = self.prime_q * self.prime_p#n

        for i in range(160):
            self.character[str(chr(i))] = self.modulus_n - i

        #print('n=',self.modulus_n)

        self.totient = (self.prime_q - 1) * (self.prime_p - 1)#tn

       # print('t=',self.totient)

        self.co_prime = self.gen_e(4)#e

        #print('e=', self.co_prime)

        

        #print("Testing co-prime")
        if(math.gcd(self.co_prime, self.totient)== 1):
            #print("Pass")
            self.private_key = self.get_key()
            #print('d=',self.private_key)
        else:
            print("Fail")
            sys.exit()
	
    def prime_gen(self, low=2, high=100):
        primes = []
        for poss in range(low, high+1):
            is_prime = True
            for num in range(low, (poss//2)+1):
                if (poss % num == 0):
                    is_prime = False
                    break
                else:
                    pass
            if (is_prime):
                primes.append(poss)
        return primes

    def gen_e(self, loops):
        e = 2
        for i in range(loops):
            while(math.gcd(self.totient, e)!=1):
                e+=1
            e+=1
        return e-1

    def get_key(self):
        d = 2
        while ((d*self.co_prime)%self.totient != 1):
            d += 1
        return d

    def encrypt_mess(self, mess):
        temp = list(mess)
        temp_num = self.get_char_num(temp)
        #print(temp_num)
        final = []
        for m in temp_num:
            final.append(int(pow(m, self.co_prime, self.modulus_n))) #C = (m^e)%n
        e_mess = " ".join(str(i) for i in final)
        return str(self.private_key) +' '+e_mess +' '+ str(self.modulus_n)

    def decrypt_mess(self, mess):
        #print('decrypting password')
        temp = mess.split(' ')
        d = int(temp[0])
        n = int(temp[-1])
        char_num = []
        message = ""
        for c in temp[1:-1]:
            char_num.append((pow(int(c), d, n)))
        #print(char_num)
        #print('converting')

        for letter in char_num:
            message += str(self.find_key_dict(letter))
        #self.queue.put(message)
        return message

    #def decrypt(self, mess):
        #self.queue = Queue()
        #d = threading.Thread(name='decrypt', target=decrypt, args=(self, mess))
        #d.start()
        #d.join()
        #return self.queue.get()

    def find_key_dict(self, a):
        for key, value in (self.character).items():
            if a == value:
                return key
        return None
        
        

    def get_char_num(self, a):
        temp = []
        for i in a:
            temp.append(self.character[i])
        return temp

    def test(self):
        test_mess = "testing this password*&(&^*"
        encrypted_mess = self.encrypt_mess(test_mess)
        print(encrypted_mess)
        decrypted_mess = self.decrypt_mess(encrypted_mess)
        print(decrypted_mess)
        
        
#main = encrypt()
#main.test()
