class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = len(nums)-1
        # nums = [2,0,2,1,1,0]       
        while white <= blue:  # 0<=5   
            curr = nums[white] # curr = nums[0] = 2
            if curr == 0:
                nums[white] = nums[red]
                nums[red] = 0
                red+=1
                white+=1
            elif curr == 1:
                white+=1
            else:
                nums[white]=nums[blue]   
                nums[blue]=2                 
                blue -=1     
                # iteration 1            
                #nums[0]=nums[5]
                #nums[5]=2
                # blue moves to index 4
                # nums=[0,0,2,1,1,2]
                # red   = 0
                # white = 0   (not incremented!)
                # blue  = 4

                #iteration 2
                # 0<=4
                # curr = nums[0] = 0
                # nums[0] = nums[0]
                # nums[red] = 0
                # red+=1 white+=1
                #nums=[0,0,2,1,1,2]
                #red=1
                #white=1
                #blue=4

                #iteration 3
                #1<=4
                #curr =nums[1]=0
                #nums[1]=nums[1]
                #nums[red]=0
                #red+=1 white+=1
                #nums=[0,0,2,1,1,2]
                #red=2  white=2 #blue =4

                #iteration 4
                #2<=4
                #curr = nums[2] = 2 
                #nums[2]=nums[4]=1
                #nums[4]=2
                #blue moves to index 3
                # nums = [0,0,1,1,2,2]
                # red =2 white =2 blue =3 

                #iteration 5
                #2<=3
                #curr= nums[2]=1
                #red=2 white = 3 blue = 3
                #nums=[0,0,1,1,2,2]

                #iteration 6
                # 3<=3
                # curr = nums[3]=1
                # red=2 whitw=4 blue=3
                #nums=[0,0,1,1,2,2]

                #iteration 7
                # 4<=3 false
                #nums = [0,0,1,1,2,2]

                # Dry Run of example 2
                # iteration 1
                # nums=[2,0,1]
                # red = 0 white =0 blue= 2
                # while(0<=2)
                # curr= nums[white] = nums[0]=2 
                # we will go in else block
                # nums[white]= nums[blue] = 1
                # nums[blue]= 2
                # move blue to index 1 
                # red = 0 white = 0 blue = 1
                # nums = [1,0,2]


                # iteration 2
                # while(0<=1)
                # curr = nums[white]= nums[0]=1
                # white+=1 white=1


                # iteration 3
                #while(1<=1)
                #curr = nums[1]=0
                #nums[1]= nums[0] =1
                # red +=1 white+=1
                # red = 1 white =2  blue =1 
                # nums= [0,1,2]

                #iteration 4
                #while(2<=1) false
                



 




        


        