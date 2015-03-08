import re
import time
import nltk
from distutils.tests.setuptools_build_ext import if_dl
from math import log
import math


def Collection_fre():
     fInput = open("files\\nsw.txt")
     #fInput = open("files\\stem.txt")
     fOutput = open("files\\Collectionfre.txt", "w")
     lines = fInput.readlines()
     Coll = {}
     term_id = {}
     id = 0
     
     for line in lines:
         Coll[line] = 0
     
     for line in lines:
         Coll[line] += 1
     
     for line in lines:
         term_id[line] = id
         id = id + 1
     
     for i in Coll:
         fOutput.write(str(i)+str(term_id[i])+"\n"+str(Coll[i])+"\n")
         
def tf_idf_term():
    #fQuery = open("files\\pre_query.txt")
    fTermMap_1 = open("files\\lexicon.txt")
    fTermMap = open("files\\pos_map.txt")
    #fTermMap = open("files\\stem_map.txt")
    fIndex_1 = open("files\\term.txt")
    fIndex = open("files\\pos.txt")
    #fIndex = open("files\\stem_index.txt")
    #fQuery = open("files\\pre_query.txt")
    #fQuery = open("files\\stem_query.txt")
    #fOriQuery = open("files\\stem_query.txt")
    fDf_1 = open("files\\df.txt")
    fDocno_1 = open("files\\Doc_map.txt")
    fDf = open("files\\pos_df.txt")
    fDocno = open("files\\Pos_Doc_map.txt")
    #fDf = open("files\\stem_df.txt")
    fDocuments = open("files\\forlanuagemodel.txt")
    fOriQuery = open("files\\pre_query.txt")
    #fOutput = open("results\\tf_idf_test.txt", "w")
    fOutput = open("results\\pos_test.txt", "w")
    #fOutput = open("results\\stem_test.txt", "w")
    fTest = open("results\\test.txt", "w")
    Documentno = fDocno.readlines()
    Documentno_1 = fDocno_1.readlines()
    documents = fDocuments.readlines()
    #query = fQuery.readlines()
    Terms = fTermMap.readlines()
    indexs = fIndex.readlines()
    df = fDf.readlines()
    #querys = fOriQuery.readlines()
    Terms_1 = fTermMap_1.readlines()
    indexs_1 = fIndex_1.readlines()
    df_1 = fDf_1.readlines()
    querys = fOriQuery.readlines()
    term_id = {}
    term_id_1 = {}
    index = []
    index_1 = []
    doc_help = []
    qlist = []
    qno = []
    #mid_help = []
    last_help = []
    doc_no = []
    q_help = []
    qhelp = []
    qnoin = []
    dff = {}
    dff_1 = {}
    Scores = {}
    Scores_1 = {}
    qid = {}
    Score_all = {}
    docno = {}
    Score_Comp = {}
    doc_len = {}
    doc_id = {}
    qlen = {}
    Term_map = {}
    docno_1 = {}
    did = 2
    id = 0
    i = 0
    count = 0
    result = 0
    first = 0
     
      #postinglist = 0
      
         
      #print Term_map
    
    for t in range(0, len(Documentno)):
          if Documentno[t].find("fr9")<0:
             docno[Documentno[t]] = Documentno[t-1]
      
    for t in range(0, len(Documentno_1)):
          if Documentno_1[t].find("fr9")<0:
             docno_1[Documentno_1[t]] = Documentno_1[t-1]
                   
    for q in querys:
          m = re.match("\d", q)
          if m:
              qno.append(q)

   
              
     
    '''
      for q in range(0, len(querys)):
          if querys[q].find("number:")>=0:
             queryid = querys[q+1]
             qlist = []
          else:
             if querys[q].find("topic:")<0 and not querys[q] in qno:
                qlist.append(querys[q])
                qid[queryid] = qlist
    '''
    for q in querys:
          m = re.match("\d{3}", q)
          if m:
              queryid = q
              qlist = []
          else:
             # q = re.sub("\n", "", q)
              qlist.append(q)
              qid[queryid] = qlist
    
    #print qid
    for q in qid:
          qlen[q] = len(qid[q])  
   # print qlen["270\n"] 
    #print len(qid["270\n"])    
    '''
      l = sorted(qid.iteritems(), key=lambda d:d[0])  
      qid = {}
      for i in range(0, len(l)):
          for j in range(0, len(l[i])):
              m = re.match("\d{3}", str(l[i][j]))
              if m:
                 qid[l[i][j]] = l[i][j+1]
    '''        
     
      
    for d in documents:
        if(d.find("fr9")>=0):
          if not d in doc_no:
            doc_no.append(d)
            doc_id[d] = did
            did = did + 1
                   
    for d in documents:
         if(d.find("fr9")<0):
            count = count + 1
         else:
            if doc_id[d] - 1>=0:
             doc_len[doc_id[d]-1] = count
             count = 0 
      
      #print qid
    
   # qnoin = ['298','313','353','374','375','376'] 
    
    for k in qid:
    #  if not k in qnoin:
        qhelp.append(k)
        qhelp.sort()
        #print qhelp    
    #for k in qid:    
    for k in qhelp:
      #if k == "270\n":
       for q in range(0,len(qid[k])):
        for d in range(0, len(df)):
              if df[d] == qid[k][q]:
                #if not query[q].isdigit():
                if  df[d+1] != 896520:
                    dff[df[d+1]] = df[d+2]
                    #print df[d+1]
       #print dff["885507\n"]
       #print dff
       for q in range(0,len(qid[k])):
        for d in range(0, len(df_1)):
              if df_1[d] == qid[k][q]:
                #if not query[q].isdigit():
                if  df_1[d+1] != 896520:
                    dff_1[df_1[d+1]] = df_1[d+2]
                    
       for i in range(0,len(qid[k])):
            for j in range(0,len(Terms)):
             # Terms[j] = re.sub("\n", "", Terms[j])
              if qid[k][i]==Terms[j]:
                   # print qid[k][i]
                   # print qid[k][i]
                  #if not Terms[j+1] in index:
                    index.append(Terms[j+1])

       for i in range(0,len(qid[k])):
            for j in range(0,len(Terms_1)):
             # Terms[j] = re.sub("\n", "", Terms[j])
              if qid[k][i]==Terms_1[j]:
                   # print qid[k][i]
                   # print qid[k][i]
                  #if not Terms[j+1] in index:
                    index_1.append(Terms_1[j+1])           
                    #fTest.write(qid[k][i]+"\n")
       
       #fTest.writelines(index)
       #for i in range(0,len(qid[k])):
       #print index
       #print indexs 
       for num in range(0,len(index)):
            for pl in range(0,len(indexs)):
              if index[num]==indexs[pl]:
               # if index[num] == "888562\n":
                 #postinglist = pl + 1
                 #tf  = re.findall("tf:[\d]{0,4}", indexs[pl+1])
                 #tf  = re.sub("tf:", "", str(tf))
                 #dno = re.findall("d:[\d]{0,4}", indexs[pl+1])
                 #dno = re.sub("d:", "", str(dno))
                 #tf_sum[index[num]] = tf
                 #dff[index[num]] = dno
                 #fOutput.write(str(indexs[pl])+" "+str(indexs[pl+1])+"\n")
                 #fOutput.write(index[num]+"\n")
                 #print len(indexs[pl+1])
                 indexstr = str(indexs[pl+1])
                 indexstring = indexstr.split(" ")
                 term_id[index[num]] = indexstring
                  #term_id[index[num]] = indexs[pl+1]
                 #print index[num] 
       
       for num in range(0,len(index_1)):
            for pl in range(0,len(indexs_1)):
              if index_1[num]==indexs_1[pl]:
               # if index[num] == "888562\n":
                 #postinglist = pl + 1
                 #tf  = re.findall("tf:[\d]{0,4}", indexs[pl+1])
                 #tf  = re.sub("tf:", "", str(tf))
                 #dno = re.findall("d:[\d]{0,4}", indexs[pl+1])
                 #dno = re.sub("d:", "", str(dno))
                 #tf_sum[index[num]] = tf
                 #dff[index[num]] = dno
                 #fOutput.write(str(indexs[pl])+" "+str(indexs[pl+1])+"\n")
                 #fOutput.write(index[num]+"\n")
                 #print len(indexs[pl+1])
                 indexstr = str(indexs[pl+1])
                 indexstring = indexstr.split(" ")
                 term_id_1[index_1[num]] = indexstring
     
       '''
       for d in documents:
        if(d.find("fr9")>=0):
          if not d in docno:
            docno.append(d)
            doc_id[d] = did
            did = did + 1
     
       for d in documents:
         if(d.find("fr9")<0):
            count = count + 1
         else:
             doc_len[doc_id[d]-1] = count
             count = 0
       '''
                  
       for i in term_id:
           for j in range(0, len(term_id[i])):
             if term_id[i][j].find("d:")>=0:
                Scores[term_id[i][j]] = 0
       
       for i in term_id_1:
           for j in range(0, len(term_id_1[i])):
             if term_id_1[i][j].find("d:")>=0:
                Scores_1[term_id_1[i][j]] = 0
      
       #count = 0
       #if i == "888562\n":
       for i in term_id:
           for j in range(0, len(term_id[i])):
             if term_id[i][j].find("d:")>=0:
              h = re.sub("d:", "", term_id[i][j])
              h = int(h)
              #print term_id[i]
              #print term_id[i]
              #print term_id[i][j]
             # pl_merge[h+int(i)] = term_id[i][j+1]
              #Scores[term_id[i][j]] += (1*log(1768/int(dff[i]))*int(term_id[i][j+1])*log(1768/int(dff[i])))/((qlen[k])*(doc_len[h])) 
              #first = (1*math.log(10, 1768/(int(dff[i])+0.5)))*(int(term_id[i][j+1]))*math.log(10,1768/(int(dff[i])+0.5))
              first = (1*log(1768/int(dff[i])))*((int(term_id[i][j+1]))*log(1768/int(dff[i])))
              second = ((qlen[k])*(doc_len[h])) 
              #result += first/second
              #Scores[term_id[i][j]] += first/second
              Scores[term_id[i][j]] += first/second
       
       for i in term_id_1:
           for j in range(0, len(term_id_1[i])):
             if term_id_1[i][j].find("d:")>=0:
              h = re.sub("d:", "", term_id_1[i][j])
              h = int(h)
              #print term_id[i]
              #print term_id[i]
              #print term_id[i][j]
             # pl_merge[h+int(i)] = term_id[i][j+1]
              #Scores[term_id[i][j]] += (1*log(1768/int(dff[i]))*int(term_id[i][j+1])*log(1768/int(dff[i])))/((qlen[k])*(doc_len[h])) 
              #first = (1*math.log(10, 1768/(int(dff[i])+0.5)))*(int(term_id[i][j+1]))*math.log(10,1768/(int(dff[i])+0.5))
              first = (1*log(1768/int(dff_1[i])))*((int(term_id_1[i][j+1]))*log(1768/int(dff_1[i])))
              second = ((qlen[k])*(doc_len[h])) 
              #result += first/second
              #Scores[term_id[i][j]] += first/second
              Scores_1[term_id_1[i][j]] += first/second
       middle = sorted(Scores_1.iteritems(), key=lambda d:d[1], reverse = True)
       #print Scores
       mid_help = sorted(Scores.iteritems(), key=lambda d:d[1], reverse = True) 
             #mid_help.append(Scores)
       #mid_help.append(result)
       #Scores = {} 
       Score_all[k] = mid_help + middle
       index = []
       term_id.clear()
       result = 0
       Scores.clear()
       #mid_help = "" 
       #mid_help = ""
    #print len(Score_all["349\n"])
    '''
    for i in Score_all:
        if len(Score_all[i]) < 100:
            Score_Comp[i] = Score_all[i]
        else:
            Score_Comp[i] = Score_all[i][:100]
    '''
    for i in Score_all:
        if len(Score_all[i]) < 100:
            Score_Comp[i] = Score_all[i]
        else:
            Score_Comp[i] = Score_all[i][:100]
    '''
    for i in Score_all:
        if len(Score_all[i]) >= 100:
            Score_Comp[i] = Score_all[i][:100]
    qhelp = []
    for i in Score_Comp:
        qhelp.append(i)
        qhelp.sort()
    '''
    '''
    for i in Score_all:
          Score_Comp[i] = Score_all[i]
    '''
    '''
    for i in Score_Comp:
        fTest.write(str(len(Score_Comp[i]))+"\n")
    '''
    '''    
      a = sorted(Score_Comp.iteritems(), key=lambda d:d[0]) 
      
      Score_Comp = {}
      for i in range(0, len(a)):
          for j in range(0, len(a[i])):
              if a[i][j] in qno:
                  Score_Comp[a[i][j]] = a[i][j+1]
       
    '''
      
    '''
      for i in Score_all:
          #for j in Score_all[i]:
          #for j in range(0, len(Score_all[i])):
              for k in range(0, len(Score_all[i])):
                  if str(Score_all[i][k]).find("d:")>=0:
                      a = re.sub("d:", "", Score_all[i][k])
                      a = int(a)
                      if a in docno:
                       b =str(i)+"0"+str(docno[a])+str(k)+str(j[k+1])+"Tfidf"+"\n"
                       fOutput.write(b)
    '''
      
    #for i in Score_Comp:
    for i in qhelp: 
       # if i == "270\n": 
        #if i == "349\n":
           for k in range(0, len(Score_Comp[i])):
              for j in range(0, len(Score_Comp[i][k])):
                  if str(Score_Comp[i][k][j]).find("d:")>=0:
                      a = re.sub("d:", "", Score_Comp[i][k][j])
                      #a = int(a)
                      #if a in docno:
                         #b =i+" "+"0"+docno[a])+" "+str(k)+" "+str(Score_all[i][k][j+1])+" "+"Tfidf"+"\n"
                      c = re.sub("\n", "", i)
                      a = a + "\n"
                      d = re.sub("\n", "", str(docno[a]))
                      b = c+" "+"0"+" "+str(d)+" "+str(k)+" "+str(Score_Comp[i][k][j+1])+" "+"Tfidf"+"\n"
                      fOutput.write(b)
start = time.clock() 
tf_idf_term()       
end = time.clock() 
print end - start            