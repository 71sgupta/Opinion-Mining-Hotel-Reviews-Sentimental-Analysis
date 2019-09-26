import os
import math
import re
import sys

path=sys.argv[1]

file=open("nbmodel.txt","r")
output=open("nboutput.txt","w")
count=0

prob_neg_decep={}
prob_neg_truth={}
prob_pos_decep={}
prob_pos_truth={}
classprob_neg_decep=0
classprob_neg_truth=0
classprob_pos_decep=0
classprob_pos_truth=0
vocabulary=[]
filedata=file.readlines()
for header in filedata[0:4]:
	header=header.replace("\n","")
	arr=header.split(" ")
	#print(arr)
	if(arr[0]=="negative" and arr[1]=="deceptive"):
		classprob_neg_decep=float(arr[2])
	elif(arr[0]=="negative" and arr[1]=="truthful"):
		classprob_neg_truth=float(arr[2])
	elif(arr[0]=="positive" and arr[1]=="deceptive"):
		classprob_pos_decep=float(arr[2])
	elif(arr[0]=="positive" and arr[1]=="truthful"):
		classprob_pos_truth=float(arr[2])

#print(classprob_neg_decep)
#print(classprob_neg_truth)
#print(classprob_pos_decep)
#print(classprob_pos_truth)

for line in filedata[4:]:
	line=line.replace("\n","")
	arr=line.split(" ")
	#print(arr)
	vocabulary.append(arr[2])
	if(arr[0]=="truthful"):
		if(arr[1]=="negative"):
			prob_neg_truth.update({arr[2]:float(arr[3])})
		elif(arr[1]=="positive"):
			prob_pos_truth.update({arr[2]:float(arr[3])})
	elif(arr[0]=="deceptive"):
		if(arr[1]=="negative"):
			prob_neg_decep.update({arr[2]:float(arr[3])})
		elif(arr[1]=="positive"):
			prob_pos_decep.update({arr[2]:float(arr[3])})
#print(arr[3])
#print(str(len(prob_pos_truth)+len(prob_pos_decep)+len(prob_neg_truth)+len(prob_neg_decep)))
vocabulary=set(vocabulary)
os.chdir(path)
cwd=os.getcwd()
stopwords=['utensils','vast','polka','mail','croissants','yogurt','following', 'away', 'barbara', 'became', 'becaue', 'because',\
'become', 'becomes', 'becoming', 'been','meridien', 'mgr', 'michigan', 'might', 'mightn', 'mightnt', 'before', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both',\
'brief', 'but', 'california','francisco', 'friday', 'from', 'further', 'furthermore','ill', 'californians', 'called', 'came', 'can',  'china', 'cig', 'come', 'comes',\
'cora', 'could', 'couldn', 'couldnt', 'coz','inward', 'iraq', 'ireland', 'ish', 'isn', 'isnt', 'italian', 'itd','pakistani', 'crt', 'december', 'did', 'didn', 'didnt', 'diego', 'dna', 'does', 'doesn', 'doesnt',\
'doing', 'don', 'done', 'dont', 'down', 'downwards', 'dublin', 'duing', 'during', 'each', 'east', 'edu', 'eight', 'either', 'else',\
'elsewhere', 'england', 'esp', 'este', 'etc', 'european', 'even', 'ever', 'everone', 'everthing', 'every', 'everytime', 'everywhere', \
'evr',  'four',  'illinois', 'inc', 'include', 'indeed', 'inn', 'into','fyi', 'get', 'gets', 'getting', 'given', 'gives', 'goes', 'going', 'gone', 'got', 'gotten', 'had', 'hadn', 'hadnt', 'happens', 'has', \
'hasn', 'hasnt', 'have', 'haven', 'havent',  'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres',\
'hereupon', 'hers', 'herself', 'hes', 'him', 'himself', 'his', 'hotel', 'houston', 'how', 'hows', 'hrh', 'hrs', 'http', 'hws', 'ian', \
'itll', 'its', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'lately', 'later', 'latter', 'latterly', 'lest', 'let', 'lets', 'london', 'looking', 'looks', 'ltd', 'manchester', 'march', 'may', 'may', 'maybe', 'mean',\
'meanwhile',  'mine', 'mon', 'monday', 'more', 'most', 'mumbai','mustn', 'mustnt', 'myself', 'name', 'namely', 'itself', 'ive', 'january', 'july', 'june', 'just','near', 'nearly', 'need', 'needn', 'neednt', 'needs', 'neither', 'nevermind', 'next',\
'october', 'off', 'office', 'often', 'ohio','west', 'weve', 'what', 'whatever', 'whats', 'when', 'whence', 'whenever', 'whens',\
'oir', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'orlando', 'osco', 'other', 'others', 'ought', 'our', 'ours', 'ourselves',\
'out', 'theyd', 'theyll', 'theyre', 'theyve', 'thier', 'think', 'third', 'this', 'those', 'though', 'thr', 'three', 'through',\
'over', 'own', 'paris', 'pda', 'penninsula', 'per', 'placed', 'ppl', 'pre', 'probably', 'que', 'quite', 'regarding',\
'restaurant', 'rri', 'said', 'same', 'san', 'saturday', 'saw', 'secondly', 'see', 'seeing',\
'hed','self','aaahed', 'canada', 'ceo', 'thur', 'thurs', 'thursday', 'thus', 'till', 'tim', 'together', 'too', 'took', 'toward', 'towards',\
'should','were', 'weren', 'werent', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'soooo', 'sooooo', 'south', 'specified', 'specify',\
'shouldn', 'shouldnt', 'shouldve', 'shouuld', 'since', 'six', 'slightly', 'some', 'somebody', 'somehow', 'someone',\
'something', 'tends', 'texas', 'than', 'that', 'thatll', 'thats', 'thats', 'thd', 'the', 'their', 'theirs', 'them', \
'specifying', 'chicago','selves', 'sent', 'september', 'seven', 'several', 'shan', 'shant', 'she', 'shed', 'shell', 'shes','spg', 'sqft', 'sta', 'still', 'sub', 'such', 'sun', 'sunday', 'sup', 'suv', 'take', 'taken', 'tell', 'ten', \
'themselves', 'then','tries', 'truly', 'try', 'trying', 'tuesday', 'tvs', 'twelveth', 'twice', 'two', 'tzu',\
'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'theres', 'thereupon', 'these', 'they', \
'thru', 'ull', 'under','seem', 'seemed', 'seeming','bangkok', 'seems', 'seen', 'abd', 'able', 'about', 'above', 'across', 'after', 'again', 'against', 'ahould', 'ain', 'aint', 'akk', 'all', 'almost', 'along', 'already', 'also', 'amd', 'america', 'american', 'among', 'amongst', 'and', 'angelas', 'angeles', 'anothers', 'any', 'anyhow', 'anymore', 'anyone', 'anyway', 'anyways', 'aother', 'app', 'appear', 'apri', 'april', 'are',\
'aren',  'way', 'wed', 'wednesday','youd',  'few', 'five', 'for', 'former', 'formerly'\
'tried', 'having', 'hawaii','whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while',\
'until', 'untill', 'upon', 'upto', 'usa', 'usd', 'use', 'used', 'uses', 'using', 'usually', 'value', 'various',\
'vegas',  'weeks', 'well','youll', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'youve','fccla', 'february', \
'went','nine', 'no', 'non', 'nor', 'north', 'not', 'november', 'now', 'nowhere', 'nyc','say', 'saying', 'says', 'seattle', 'second',  \
'where', 'whither', 'who', 'whoever', 'arent', 'around', 'aside', 'atlanta', 'atleast', 'august','very', 'via', 'viz', 'want', 'wants', 'was', 'wasn', 'wasnt','whole', 'whom', 'whos', 'whose', 'why', 'whys', 'will', 'willing', 'wisconsin', 'wish',\
'with', 'within', 'without', 'won', 'wont', 'woudl', 'would', 'wouldn', 'wouldnt', 'writte', 'yet', 'york', 'you',\
]

count=0
#print(len(vocabulary))
for i in os.listdir(os.getcwd()):
	if(os.path.isdir(i)):
		os.chdir(cwd+"/"+str(i))
		for j in os.listdir(os.getcwd()):
			if(os.path.isdir(j)):
				os.chdir(cwd+"/"+str(i)+"/"+str(j))
				for k in os.listdir(os.getcwd()):
					if(os.path.isdir(k)):
						os.chdir(cwd+"/"+str(i)+"/"+str(j)+"/"+str(k))
						for l in os.listdir(os.getcwd()):
							count=count+1
							if(os.path.isfile(l) and l.endswith(".txt")):
								neg_dec=0
								neg_truth=0
								pos_dec=0
								pos_truth=0
								f=open(l,"r")
								test=str(f.read())
								test=test.lower()
								#print(test[0:10])
								test=re.sub('[^A-Za-z]', ' ', test)
								test=test.split(" ")
								test2=[p for p in test if(p not in stopwords)]
								test1=[q for q in test2 if(len(q)>2)]
								for m in test1:
									if(m in vocabulary):
										neg_dec=neg_dec+math.log(prob_neg_decep[m])
										neg_truth=neg_truth+math.log(prob_neg_truth[m])
										pos_dec=pos_dec+math.log(prob_pos_decep[m])
										pos_truth=pos_truth+math.log(prob_pos_truth[m])

								result=[]
								result.append(neg_dec+math.log(classprob_neg_decep))
								result.append(neg_truth+math.log(classprob_neg_truth))
								result.append(pos_dec+math.log(classprob_pos_decep))
								result.append(pos_truth+math.log(classprob_pos_truth))
								
								index=result.index(max(result))
								temp=""
								if(index==0):
									temp="deceptive negative "+cwd+"/"+str(i)+"/"+str(j)+"/"+str(k)+"/"+str(l)+"\n"
								elif(index==1):
									temp="truthful negative "+cwd+"/"+str(i)+"/"+str(j)+"/"+str(k)+"/"+str(l)+"\n"
								elif(index==2):
									temp="deceptive positive "+cwd+"/"+str(i)+"/"+str(j)+"/"+str(k)+"/"+str(l)+"\n"
								elif(index==3):
									temp="truthful positive "+cwd+"/"+str(i)+"/"+str(j)+"/"+str(k)+"/"+str(l)+"\n"
								output.write(temp)
						os.chdir(cwd+"/"+str(i)+"/"+str(j))
				os.chdir(cwd+"/"+str(i))
		os.chdir(cwd)
#print(count)