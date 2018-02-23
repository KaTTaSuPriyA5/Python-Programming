def main():
 a=str(input())

 if(str(a)==str(a[::-1])):
    print("palindrome")
 else:
    print("not a palindrome")
if __name__ == '__main__':
    main()
