def TwoSumApproach2(self, nums: list[int], target: int) -> list[int]:
    print(nums)
    for i in range(len(nums)):
        a=target-nums[i]
        if a in nums[i+1:]:
            return([i,nums.index(a,i+1)])
        else:
            continue

def TwoSumApproach1(self, nums: list[int], target: int) -> list[int]:
    num1index=0
    while(True):
        count=len(nums)
        for num in range(num1index+1,count):
            if nums[num]+nums[num1index]-target==0:
                num2index=num
                return([num1index,num2index])
        num1index+=1

print(TwoSumApproach2(__name__,[2,7,11,15],9))
print(TwoSumApproach1(__name__,[2,7,11,15],9))            
