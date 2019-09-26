import os
import math
import re
import sys

path=sys.argv[1]
modelfile=open("nbmodel.txt","w")
os.chdir(path)

negative_truthful=""
positive_truthful=""
negative_deceptive=""
positive_deceptive=""

cwd=os.getcwd()
fullpath=cwd
count=0
count1=0
count2=0
count3=0
count4=0
for i in os.listdir(cwd):
	if(os.path.isdir(i)):
		if("negative" in i.lower().split("_")):
			os.chdir(cwd+"/"+str(i))
			for j in os.listdir(os.getcwd()):
				if(os.path.isdir(j)):
					if("deceptive" in j.lower().split("_")):
						os.chdir(cwd+"/"+str(i)+"/"+str(j))
						for k in os.listdir(os.getcwd()):
							if(os.path.isdir(k)):
								os.chdir(cwd+"/"+str(i)+"/"+str(j)+"/"+str(k))
								#print(os.getcwd())
								for l in os.listdir(os.getcwd()):
									if(os.path.isfile(l) and l.endswith(".txt")):
										count=count+1
										f=open(l,"r")
										negative_deceptive=negative_deceptive+" "+str(f.read())
										count1=count1+1;
								os.chdir(cwd+"/"+str(i)+"/"+str(j))
					elif("truthful" in j.lower().split("_")):
						os.chdir(cwd+"/"+str(i)+"/"+str(j))
						for k in os.listdir(os.getcwd()):
							if(os.path.isdir(k)):
								os.chdir(cwd+"/"+str(i)+"/"+str(j)+"/"+str(k))
								#print(os.getcwd())
								for l in os.listdir(os.getcwd()):
									if(os.path.isfile(l) and l.endswith(".txt")):
										count=count+1
										f=open(l,"r")
										negative_truthful=negative_truthful+" "+str(f.read())
										count2=count2+1;
								os.chdir(cwd+"/"+str(i)+"/"+str(j))
					os.chdir(cwd+"/"+str(i))

		elif("positive" in i.lower().split("_")):
			os.chdir(cwd+"/"+str(i))
			for j in os.listdir(os.getcwd()):
				if(os.path.isdir(j)):
					if("deceptive" in j.lower().split("_")):
						os.chdir(cwd+"/"+str(i)+"/"+str(j))
						for k in os.listdir(os.getcwd()):
							if(os.path.isdir(k)):
								os.chdir(cwd+"/"+str(i)+"/"+str(j)+"/"+str(k))
								#print(os.getcwd())
								for l in os.listdir(os.getcwd()):
									if(os.path.isfile(l) and l.endswith(".txt")):
										count=count+1
										f=open(l,"r")
										positive_deceptive=positive_deceptive+" "+str(f.read())
										count3=count3+1;
								os.chdir(cwd+"/"+str(i)+"/"+str(j))
					elif("truthful" in j.lower().split("_")):
						os.chdir(cwd+"/"+str(i)+"/"+str(j))
						for k in os.listdir(os.getcwd()):
							if(os.path.isdir(k)):
								os.chdir(cwd+"/"+str(i)+"/"+str(j)+"/"+str(k))
								#print(os.getcwd())
								for l in os.listdir(os.getcwd()):
									if(os.path.isfile(l) and l.endswith(".txt")):
										count=count+1
										f=open(l,"r")
										positive_truthful=positive_truthful+" "+str(f.read())
										count4=count4+1;
								os.chdir(cwd+"/"+str(i)+"/"+str(j))
					os.chdir(cwd+"/"+str(i))
		os.chdir(cwd)
'''
print(str(negative_deceptive[0:1000]))
print(len(negative_truthful))	
print(len(positive_deceptive))
print(len(positive_truthful))
'''

totalcount=count1+count2+count3+count4
prob1=float(count1)/totalcount

prob2=float(count2)/totalcount

prob3=float(count3)/totalcount

prob4=float(count4)/totalcount

negative_deceptive=negative_deceptive.lower()
negative_deceptive=re.sub('[^A-Za-z]', ' ', negative_deceptive)
negative_deceptive=negative_deceptive.split(" ")

#print(str(negative_deceptive[0:1000]))


negative_truthful=negative_truthful.lower()
negative_truthful=re.sub('[^A-Za-z]', ' ', negative_truthful)
negative_truthful=negative_truthful.split(" ")


positive_deceptive=positive_deceptive.lower()
positive_deceptive=re.sub('[^A-Za-z]', ' ', positive_deceptive)
positive_deceptive=positive_deceptive.split(" ")


positive_truthful=positive_truthful.lower()
positive_truthful=re.sub('[^A-Za-z]', ' ', positive_truthful)
positive_truthful=positive_truthful.split(" ")



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


neg_decep_sw=[i for i in negative_deceptive if (i not in stopwords)]

neg_truth_sw=[i for i in negative_truthful if (i not in stopwords)]

pos_decep_sw=[i for i in positive_deceptive if (i not in stopwords)]

pos_truth_sw=[i for i in positive_truthful if (i not in stopwords)]

neg_decep_sw=[i for i in neg_decep_sw if (len(i)>2)]

neg_truth_sw=[i for i in neg_truth_sw if (len(i)>2)]

pos_decep_sw=[i for i in pos_decep_sw if (len(i)>2)]

pos_truth_sw=[i for i in pos_truth_sw if (len(i)>2)]

unique_neg_decep=set(neg_decep_sw)

unique_neg_truth=set(neg_truth_sw)

unique_pos_decep=set(pos_decep_sw)

unique_pos_truth=set(pos_truth_sw)

vocabulary=[]
for i in unique_neg_decep:
	vocabulary.append(i)

for i in unique_neg_truth:
	vocabulary.append(i)

for i in unique_pos_decep:
	vocabulary.append(i)

for i in unique_pos_truth:
	vocabulary.append(i)
#print(len(vocabulary))

vocabulary=set(vocabulary)

#print(len(vocabulary))


count_neg_decep={}
count_neg_truth={}
count_pos_decep={}
count_pos_truth={}

voc_size=len(vocabulary)


for i in vocabulary:
	count_neg_decep.update({i:neg_decep_sw.count(i)})
'''
print(sum(count_neg_decep.values()))
print(len(neg_decep_sw))
'''

for i in vocabulary:
	count_neg_truth.update({i:neg_truth_sw.count(i)})

#print(sum(count_neg_truth.values()))
#print(len(neg_truth_sw))


for i in vocabulary:
	count_pos_decep.update({i:pos_decep_sw.count(i)})

#print(sum(count_pos_decep.values()))
#print(len(pos_decep_sw))

for i in vocabulary:
	count_pos_truth.update({i:pos_truth_sw.count(i)})

#print(sum(count_pos_truth.values()))
#print(len(pos_truth_sw))


#print(str(len(count_pos_truth)+len(count_pos_decep)+len(count_neg_truth)+len(count_neg_decep)))

modelfile.write("negative deceptive "+str(prob1)+"\n")
modelfile.write("negative truthful "+str(prob2)+"\n")
modelfile.write("positive deceptive "+str(prob3)+"\n")
modelfile.write("positive truthful "+str(prob4)+"\n")

prob_neg_decep={}
prob_neg_truth={}
prob_pos_decep={}
prob_pos_truth={}

class1=float(sum(count_neg_decep.values())+voc_size)

for x,y in count_neg_decep.items():
	temp=((y+1)/class1)
	prob_neg_decep.update({x:temp})
	modelfile.write("deceptive negative "+str(x)+" "+str(temp)+"\n")
# not coming 1 and what about class prob is it same
#print(sum(prob_neg_decep.values()))


class2=float(sum(count_neg_truth.values())+voc_size)

for x,y in count_neg_truth.items():
	temp=((y+1)/class2)
	prob_neg_truth.update({x:temp})
	modelfile.write("truthful negative "+str(x)+" "+str(temp)+"\n")
#print(sum(prob_neg_truth.values()))

class3=float(sum(count_pos_decep.values())+voc_size)

for x,y in count_pos_decep.items():
	temp=((y+1)/class3)
	prob_pos_decep.update({x:temp})
	modelfile.write("deceptive positive "+str(x)+" "+str(temp)+"\n")

#print(sum(prob_pos_decep.values()))

class4=float(sum(count_pos_truth.values())+voc_size)
tempvar=""
for x,y in count_pos_truth.items():
	temp=((y+1)/class4)
	prob_pos_truth.update({x:temp})
	tempvar=tempvar+"truthful positive "+str(x)+" "+str(temp)+"\n"
modelfile.write(tempvar[:-1])

modelfile.write("\n")

modelfile.close()
#print(sum(prob_pos_truth.values()))


















































































































































































