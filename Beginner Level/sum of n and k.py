def main():
  n=int(input())
  arr = [ int(input()) for i in range(n)]
  k=int(input())
  for i in range(0,k):
    su=0
    su=su+arr[i+1]
  print(su)
if __name__ == '__main__':
    main()
