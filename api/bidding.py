import numpy as np
from scipy import stats

""" def calculateBiddingScore(myBid: float, bids: list[float]) -> dict:
    if (myBid not in bids):
        raise ValueError("myBid not in bids")
    # 基准价分数
    baseBidScore = 100
    bids = np.array(bids)
    lowestBid = bids.min() #最低价
    highestBid = bids.max() #最高价
    bidDiff = highestBid - lowestBid # 最高价和最低价的差
    # 投标区间
    firstSection = bids[bids <= lowestBid + bidDiff / 3]
    secondSection = bids[(bids > lowestBid + bidDiff / 3) & (bids <= lowestBid + bidDiff * 2 / 3)]
    thirdSection = bids[bids > lowestBid + bidDiff * 2 / 3]
    # 区间代表价
    firstBidRep = np.average(firstSection)
    secondBidRep = np.average(secondSection)
    thirdBidRep = np.average(thirdSection) 
    bidReps = np.array([firstBidRep, secondBidRep, thirdBidRep])
    # 评标基准价
    baseBid = 0.99 * bidReps.sum() / np.count_nonzero(bidReps)
    # 计算投标评分
    diffFromBaseBidCoeff = -1 if myBid > baseBid else 0.5 # 与基准竞标价差值的减分系数
    numofRoundDigits = 2 #保留2位小数
      
    bidScores = {}
    for bid in bids:
        if bid > baseBid:
          bidScores[bid] = round(baseBidScore - diffFromBaseBidCoeff*(bid - baseBid) / baseBid, numofRoundDigits)
        else:
          bidScores[bid] = round(baseBidScore - diffFromBaseBidCoeff*(baseBid - bid) / baseBid, numofRoundDigits)
    
    # 计算我的对应竞标价分数
            
    return bidScores """
def calculateBaselineIntervals(numOfBid,lowestBid,highestBid):
    numOfBid = int(numOfBid)
    lowestBid = float(lowestBid)
    highestBid = float(highestBid)
    
    myBid = np.linspace(lowestBid, highestBid, 1000)
    bidStd = 1
    bidMean = (lowestBid + highestBid) / 2
    bidDistribution = stats.norm(bidMean, bidStd)
    bidsArr = np.array([bidStd]* numOfBid)
    baselineMean = bidDistribution.mean()
    baselineStd = np.sqrt(np.sum(bidsArr**2) / numOfBid**2)
    baselineDistribution = stats.norm(0.99*baselineMean, baselineStd)
    highConfidenceInterval = baselineDistribution.interval(0.95)
    return highConfidenceInterval

# main function in python
if __name__ == "__main__":
    # take an argument
    numOfBid = int(input("竞标数量（可变竞标价数量）："))
    lowestBid = float(input("可能最低竞标价："))
    highestBid = float(input("可能最大竟标价："))
    myBid = np.linspace(lowestBid, highestBid, 1000)
    bidStd = 1
    bidMean = (lowestBid + highestBid) / 2
    bidDistribution = stats.norm(bidMean, bidStd)
    bidsArr = np.array([bidStd]* numOfBid)
    baselineMean = bidDistribution.mean()
    baselineStd = np.sqrt(np.sum(bidsArr**2) / numOfBid**2)
    baselineDistribution = stats.norm(0.99*baselineMean, baselineStd)
    highConfidenceInterval = baselineDistribution.interval(0.95)
    print("统计上竞标基准值有95% 可能性存在于此范围： (" +str(highConfidenceInterval[0]) +"," + str(highConfidenceInterval[1]) +")")
    print("最佳区间尽可能取值在：("+str(highConfidenceInterval[0]) +"," + str(np.average(highConfidenceInterval)) +"),并 靠近 "+ str(np.average(highConfidenceInterval)))
    # print("可能性竞标基准值在这个区间：" + baselineDistribution.interval(0.95))
    # print("最佳区间尽可能取值在" + baselineDistribution.inerval(0.95)[0] +"到"+ baselineDistribution.inerval(0.95)[1] /2)
    