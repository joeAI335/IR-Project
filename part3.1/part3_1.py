import time
import re
import math
from math import log

def term():
       fInput = open("files\\nsw.txt")
       fOutput = open("files\\term.txt", "w")
       fTest = open('test.txt', "w")
       lines = fInput.readlines()
       id = 0
       tf = 0
       did = 0
       count = 0
       term = {}
       term_tf = {}
       term_id = {}
       term_did = {} 
       term_help = {}
       docno = []
       term_col = []
       del_line = []
      
       for line in lines:
        if(line.find("fr9")>=0):
          if not line in docno:
            docno.append(line)
       
       
       
       for line in lines:
           term_id[line] = id
           id = id + 1
       
       for line in lines:
        if not line in docno:
         term[line] = " "
         term_tf[line] = 0
       '''  
       for did in range(0,len(docno)+1):
         term_tf[did] = tf 
      '''
           
       for line in lines:
        if not line in docno:
           term_did[line] = did
           term_tf[line] += 1
           term[line] += " "+"d:"+str(term_did[line])+" "+str(term_tf[line])
           #fOutput.write(str(term_id[line])+"\n"+str(term_did[line])+"\n"+str(term_tf[term_did[line]])+"\n")
        else:
           for key in term:
              term_tf[key] = 0
           if not line in del_line:
              del_line.append(line)
              did = did + 1
           count = 0
       
       
       for key in term:
           if term_id[key] != 896520: 
             fOutput.write(str(term_id[key])+"\n"+term[key]+"\n")
def new_index():
    fInput = open("files\\term.txt")
    fOutput = open("new.txt", "w")
    lines = fInput.readlines()
    index = {}
    indexs = {}
    str = ""
    
    for i in range(0, len(lines)):
        if lines[i].find("d")<0:
         indexs[lines[i]] = ""
        
    for i in range(0, len(lines)):
     # if lines[i] == "373040\n":
        if lines[i].find("d:")<0:
            newline = lines[i+1].split(" ")
            for j in range(0, len(newline)):
                if newline[j].find("d:")>=0:
                    newline[j+1] = re.sub("\n", "", newline[j+1])
                    index[newline[j]] = newline[j+1]
            mid_help = sorted(index.iteritems(), key=lambda d:d[1], reverse = True)
            j = 2
            for m in mid_help:
             if j <= 4:
                for k in range(0, len(m)):
                  if m[k].find("d:")>=0:
                       indexs[lines[i]] += " "+m[k]+" "+m[k+1]
                       j += 1
            
                    #print lines[i]
            #indexs[lines[i]] = mid_help
            #fOutput.write(mid_help)    
        '''
            for k in index:
                indexs[lines[i]] += " "+k + " " +index[k] 
        ''' 
                
            #mid_help = sorted(index.iteritems(), key=lambda d:d[1], reverse = True) 
            #print mid_help
        '''
            for k in index:
                #str = " " + k + " " + index[k]
                indexs[lines[i]] = " "
        '''    
            #indexs[lines[i]] = mid_help
        '''
            for m in mid_help:
                #indexs[lines[i]] += " "+str(m)  + " "+ str(index[m])
                #indexs[lines[i]] += str 
                for k in range(0, len(m)):
                    if m[k].find("d:")>=0:
                       indexs[lines[i]] += " "+str(m[k])+ " "+ str(m[k+1])
        '''
            #indexs[lines[i]] = mid_help
        '''
            for m in mid_help:
                for k in range(0, len(m)):
                    if m[k].find("d:")>=0:
                       fOutput.write(m[k]+" "+m[k+1]+"\n")
            #fOutput.write(str(mid_help)+"\n")
        '''
        index= {}       
    
    
    #print indexs.values()
    #j = 0
    for i in indexs:
       
        #print indexs[i]
        #print indexs
        #print indexs[i]
        #if i.find("d:")<0:
           fOutput.write(i+indexs[i]+"\n")
           
           
    
    #fOutput.write(str(mid_help))
def cal_stem():
       fInput = open("files\\Stem.txt")
       fOutput = open("files\\Stem_index.txt", "w")
       lines = fInput.readlines()
       id = 0
       tf = 0
       did = 0
       term = {}
       term_tf = {}
       term_id = {}
       term_did = {} 
       term_help = {}
       docno = []
       term_col = []
       del_line = []
      
       for line in lines:
        if(line.find("fr9")>=0):
          if not line in docno:
            docno.append(line)
       
       for line in lines:
        if not line in docno:
         term[line] = " "
         term_tf[line] = tf 
       
       for line in lines:
           term_id[line] = id
           id = id + 1
       
      
           
       for line in lines:
        if not line in docno:
           term_did[line] = did
           term_tf[line] += 1
           term[line] += " "+"d:"+str(term_did[line])+" "+str(term_tf[line])
        else:
           for key in term:
              term_tf[key] = 0
           if not line in del_line:
              del_line.append(line)
              did = did + 1
        
       for key in term:
             fOutput.write(str(term_id[key])+"\n"+term[key]+"\n")

def cal_pos():
    fInput = open("files\\Pre-process.txt")
    fOutput = open("files\\pos.txt", "w")
    lines = fInput.readlines()
    term_id = {}
    term_pos = {}
    term_docid = {}
    term = {}
    docno = []
    del_line = []
    pos = 1
    did = 0
    id = 0
    for line in lines:
        if(line.find("fr9")>=0):
          if not line in docno:
            docno.append(line)
    
    for line in lines:
           term_id[line] = id
           id = id + 1
    
    for line in lines:
           term[line] = " "
    for line in lines:
        if not line in docno:
           term_pos[line] = pos
           pos = pos + 1
           term_docid[line] = did
           term[line] += " "+"d:"+str(term_docid[line])+" "+str(term_pos[line])
        else:
           pos = 0
           if not line in del_line:
              del_line.append(line)
              did = did + 1
    for key in term:
        if term_id[key] != 896520:
             fOutput.write(str(term_id[key])+"\n"+term[key]+"\n")

def cal_phrase():
    fInput = open("files\\pre-process.txt")
    fOutput = open("files\\phrase_index.txt", "w")
    fStops = open("files\\stops.txt")
    lines = fInput.readlines()
    stops = fStops.readlines()
    docno = []
    phrases = []
    del_line = []
    line_id = 0
    phrase_id = 0
    ph_id = {}
    term_id = {}
    phrase = {}
    phr = {}
    phrase_tf = {}
    phrase_did = {}
    oriline = {}
    stop = {}
    id = 0
    did = 0
    
    for i in stops:
        stop[i] = id
        id = id + 1
    
    for line in lines:
        if(line.find("fr9")>=0):
          if not line in docno:
            docno.append(line)

    for line in lines:
        oriline[line_id] = line
        line_id = line_id + 1

    for keys in oriline:
      if keys + 1 in oriline:
       punc_1 = re.match("/W+", oriline[keys])
       punc_2 = re.match("/W+", oriline[keys+1])
       if not punc_1 and not punc_2:
         if not oriline[keys] in stop:
            if not oriline[keys+1] in stop:
              phrases.append(oriline[keys] + oriline[keys+1])
    
    for phrase in phrases:
       if(phrase.find("fr9")<0):
           ph_id[phrase] = phrase_id
           phrase_id = phrase_id + 1
           phr[phrase] = " "
           phrase_tf[phrase] = 0
    
    for phrase in phrases:
        if(phrase.find("fr9")<0):
           phrase_did[phrase] = did
           phrase_tf[phrase] += 1
           phr[phrase] += " "+"d:"+str(phrase_did[phrase])+" "+str(phrase_tf[phrase])
           #fOutput.write(str(term_id[line])+"\n"+str(term_did[line])+"\n"+str(term_tf[term_did[line]])+"\n")
        else:
           for key in phr:
              phrase_tf[key] = 0
           if not phrase in del_line:
              del_line.append(phrase)
              did = did + 1
       
    for key in phr:
           #if phrase_id[key] != 896520: 
             fOutput.write(str(ph_id[key])+"\n"+str(phr[key])+"\n")

def test():
    fInput = open("term.txt")
    fOutput = open("new.txt", "w")
    lines = fInput.readlines()
    index = {}
    indexs = {}
    
    for i in range(0, len(lines)):
        indexs[lines[i]] = ""
    
    for i in range(0, len(lines)):
        if lines[i].find("d:")<0:
            newline = lines[i+1].split(" ")
            for j in range(0, len(newline)):
                if newline[j].find("d:")>=0:
                    index[newline[j]] = newline[j+1]
            
            for m in index:
                indexs[lines[i]] += " "+str(m)  + " "+ str(index[m])
        index = {}
        
    for i in indexs:
        fOutput.write(str(i)+str(indexs[i])+"\n")
                        
def tf_idf_term():
    #fQuery = open("files\\pre_query.txt")
    fTermMap = open("files\\lexicon.txt")
    #fTermMap = open("files\\pos_map.txt")
    #fTermMap = open("files\\stem_map.txt")
    fIndex = open("new.txt")
    #fIndex = open("files\\pos.txt")
    #fIndex = open("files\\stem_index.txt")
    #fQuery = open("files\\pre_query.txt")
    #fQuery = open("files\\stem_query.txt")
    #fOriQuery = open("files\\stem_query.txt")
    fDf = open("files\\df.txt")
    fDocno = open("files\\Doc_map.txt")
    #fDf = open("files\\pos_df.txt")
    #fDocno = open("files\\Pos_Doc_map.txt")
    #fDf = open("files\\stem_df.txt")
    fDocuments = open("files\\forlanuagemodel.txt")
    fOriQuery = open("files\\nsw_query.txt")
    fOutput = open("results\\tf_idf_test.txt", "w")
    #fOutput = open("results\\pos_test.txt", "w")
    #fOutput = open("results\\stem_test.txt", "w")
    fTest = open("results\\test.txt", "w")
    Documentno = fDocno.readlines()
    documents = fDocuments.readlines()
    #query = fQuery.readlines()
    Terms = fTermMap.readlines()
    indexs = fIndex.readlines()
    df = fDf.readlines()
    querys = fOriQuery.readlines()
    term_id = {}
    index = []
    doc_help = []
    qlist = []
    qno = []
    #mid_help = []
    last_help = []
    doc_no = []
    q_help = []
    qhelp = []
    qnoin = []
    querymid = []
    dff = {}
    Scores = {}
    qid = {}
    Score_all = {}
    docno = {}
    Score_Comp = {}
    doc_len = {}
    doc_id = {}
    qlen = {}
    Term_map = {}
    pl_merge = {}
    Score_q = {}
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
              #print len(qlist)
              #percent = int(len(qlist)/2)
              qid[queryid] = qlist#[0:3]
    
    #print qid
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
    #print doc_len[959]
      #print qid
    
   # qnoin = ['298','313','353','374','375','376'] 
    
    for m in qid:
      #if m == "288\n":
        for q in range(0, len(qid[m])):
           for d in range(0, len(df)):
            if df[d] == qid[m][q]:
                #if not query[q].isdigit():
                if  df[d+1] != 896520:
                    dff[df[d+1]] = df[d+2]
        for i in range(0,len(qid[m])):
            for j in range(0,len(Terms)):
             # Terms[j] = re.sub("\n", "", Terms[j])
              if qid[m][i]==Terms[j]:
                   # print qid[k][i]
                   # print qid[k][i]
                  #if not Terms[j+1] in index:
                    index.append(Terms[j+1])
                    Score_q[qid[m][i]] = 1768/int(dff[Terms[j+1]])
        query_help = sorted(Score_q.iteritems(), key=lambda d:d[1], reverse = False)    
        for w in range(0, len(query_help)):
            for u in range(0, len(query_help[w])):
                if not str(query_help[w][u]).isdigit():
                    querymid.append(query_help[w][u])
        qid[m] = querymid[0:3]  
        querymid = []
        Score_q.clear()
    
        
    for k in qid:
    #  if not k in qnoin:
        qhelp.append(k)
        qhelp.sort()
        #print qid[k]
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
       for i in range(0,len(qid[k])):
            for j in range(0,len(Terms)):
             # Terms[j] = re.sub("\n", "", Terms[j])
              if qid[k][i]==Terms[j]:
                   # print qid[k][i]
                   # print qid[k][i]
                  #if not Terms[j+1] in index:
                    index.append(Terms[j+1])
                    
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
       #print Scores
       mid_help = sorted(Scores.iteritems(), key=lambda d:d[1], reverse = True) 
             #mid_help.append(Scores)
       #mid_help.append(result)
       #Scores = {} 
       Score_all[k] = mid_help
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

def Score_BM25():
     #fQuery = open("files\\pre_query.txt")
     fTermMap = open("files\\lexicon.txt")
     #fTermMap = open("files\\stem_map.txt")
     fIndex = open("new.txt")
     #fIndex = open("files\\stem_index.txt")
     fDf = open("files\\df.txt")
     #fDf = open("files\\stem_df.txt")
     #fOriQuery = open("files\\stem_query.txt")
     #fDocuments = open("pre-process.txt")
     fDocuments = open("files\\forlanuagemodel.txt")
     fOriQuery = open("files\\nsw_query.txt")
     fDocno = open("files\\Doc_map.txt")
     fOutput = open("results\\testBM25.txt", "w")
     #query = fQuery.readlines()
     Terms = fTermMap.readlines()
     indexs = fIndex.readlines()
     df = fDf.readlines()
     documents = fDocuments.readlines()
     querys = fOriQuery.readlines()
     Documentno = fDocno.readlines()
     term_id = {}
     tf_sum = {}
     doc_id = {}
     doc_tf = {}
     doc_term_dl = {}
     index = []
     plist = []
     doc_help = []
     doc_term_len = []
     qno = []
     doc_no = []
     qhelp = []
     querymid = []
     dff = {}
     Scores = {}
     qtf= {}
     qid = {}
     doc_len = {}
     Score_all = {}
     Score_Comp = {}
     docno = {}
     Score_q = {}
     qf = 1
     id = 0
     i = 0
     totallen = 0
     did = 1
     count = 0
     k1 = 1.2
     k2 = 500
     b = 0.75
     R = 0.0
     r = 0
     N = 1768
     avdl = 0
     n = 0
           
     for t in range(0, len(Documentno)):
          if Documentno[t].find("fr9")<0:
             docno[Documentno[t]] = Documentno[t-1]  
     
     
     for d in documents:
        if(d.find("fr9")>=0):
          if not d in docno:
            doc_no.append(d)
            doc_id[d] = did
            did = did + 1
            
    
     for d in documents:
         if(d.find("fr9")<0) and d != "\n":
            count = count + 1
         else:
            if(d.find("fr9")>=0):
             doc_len[doc_id[d]] = count
             count = 0
     
     for d in documents:
         m = re.match("\w", d)
         if d.find("fr9")<0 and m:
            totallen += 1 
     
     avdl = totallen/1768
     '''
     for d in documents:
         if d.find("fr9")<0:
            doc_help.append(d)
            count = count + 1
         else:
            list_c = []
            list_c = [d for d in doc_help if d in query]
            if len(list_c)>0:
              for i in list_c:
               doc_term_len.append(count)
               doc_term_dl[i] = doc_term_len
            else:
              doc_term_len = []
              count = 0
              doc_help = []
     '''
     for q in querys:
          m = re.match("\d", q)
          if m:
              qno.append(q)
     
     for q in querys:
          m = re.match("\d{3}", q)
          if m:
              queryid = q
              qlist = []
          else:
              qlist.append(q)
              qid[queryid] = qlist
     ''' 
     l = sorted(qid.iteritems(), key=lambda d:d[0])  
     qid = {}
     for i in range(0, len(l)):
          for j in range(0, len(l[i])):
              m = re.match("\d{3}", str(l[i][j]))
              if m:
                 qid[l[i][j]] = l[i][j+1]
     '''         
     
    
     
     
     '''          
       for q in range(0,len(qid[k])):
        for d in range(0, len(df)):
              if df[d] == query[q] and query[q] != "number":
                if not query[q].isdigit():
                 if not df[d+1] == 896520:
                   dff[df[d+1]] = df[d+2]
     '''
     for m in qid:
      #if m == "288\n":
        for q in range(0, len(qid[m])):
           for d in range(0, len(df)):
            if df[d] == qid[m][q]:
                #if not query[q].isdigit():
                if  df[d+1] != 896520:
                    dff[df[d+1]] = df[d+2]
        for i in range(0,len(qid[m])):
            for j in range(0,len(Terms)):
             # Terms[j] = re.sub("\n", "", Terms[j])
              if qid[m][i]==Terms[j]:
                   # print qid[k][i]
                   # print qid[k][i]
                  #if not Terms[j+1] in index:
                    index.append(Terms[j+1])
                    Score_q[qid[m][i]] = 1768/int(dff[Terms[j+1]])
        query_help = sorted(Score_q.iteritems(), key=lambda d:d[1], reverse = False)    
        for w in range(0, len(query_help)):
            for u in range(0, len(query_help[w])):
                if not str(query_help[w][u]).isdigit():
                    querymid.append(query_help[w][u])
        qid[m] = querymid[0:3]  
        querymid = []
        Score_q.clear()
     
    
     for k in qid:
      #if not k in qnoin:
        qhelp.append(k)
        qhelp.sort()
        #print qhelp             
    # for k in qid:
     #print qhelp
     for k in qhelp:
      for q in range(0,len(qid[k])):
        for d in range(0, len(df)):
              if df[d] == qid[k][q]: #and query[q] != "number":
                #if not query[q].isdigit():
                 if not df[d+1] == 896520:
                   dff[df[d+1]] = df[d+2]   
                   #n = dff[k]     
                      
      '''
      for i in range(0,len(query)):
          for j in range(0,len(Terms)):
              if query[i]==Terms[j]:
                 index.append(Terms[j+1])
      '''
      for i in range(0,len(qid[k])):
            for j in range(0,len(Terms)):
                if qid[k][i]==Terms[j]:
                    index.append(Terms[j+1])
      
      for num in range(0,len(index)):
          for pl in range(0,len(indexs)):
              if index[num]==indexs[pl]:
                 indexstr = str(indexs[pl+1])
                 indexstr = indexstr.split(" ")
                 term_id[index[num]] = indexstr
            
      for i in term_id:
           for j in range(0, len(term_id[i])):
             if term_id[i][j].find("d:")>=0:
                Scores[term_id[i][j]] = 0
                 
      for i in term_id:
          for j in range(0, len(term_id[i])):
             if term_id[i][j].find("d:")>=0:
               did = re.sub("d:", "", term_id[i][j])
               did = int(did)
               f = (int)(term_id[i][j+1])
               #if did in doc_len:
               K = k1 * ((1-b) + b * int(doc_len[did]/avdl))
                #first = log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)) )
               first = log((1768-int(dff[i])+0.5)/(int(dff[i])+0.5))
               second = ((k1 + 1) * f) / (K + f)
               third = ((k2+1) * qf) / (k2 + qf)
               Scores[term_id[i][j]] += first*second*third 
      
      mid_help = sorted(Scores.iteritems(), key=lambda d:d[1], reverse = True) 
             #mid_help.append(Scores)
      index = []
      term_id.clear()   
      Score_all[k] = mid_help
      Scores.clear()
      #print Score_all
       #mid_help = "" 
     '''
     for i in Score_all:
          Score_Comp[i] = Score_all[i][:100]
     '''
     for i in Score_all:
        if len(Score_all[i]) < 100:
            Score_Comp[i] = Score_all[i]
        else:
            Score_Comp[i] = Score_all[i][:100]
     '''    
     a = sorted(Score_Comp.iteritems(), key=lambda d:d[0]) 
      
     
     for i in range(0, len(a)):
          for j in range(0, len(a[i])):
              if a[i][j] in qno:
                  Score_Comp[a[i][j]] = a[i][j+1]
     '''
    
    # for i in Score_Comp:
     for i in qhelp:
           for k in range(0, len(Score_Comp[i])):
              for j in range(0, len(Score_Comp[i][k])):
                 if str(Score_Comp[i][k][j]).find("d:")>=0:
                      a = re.sub("d:", "", Score_Comp[i][k][j])
                      a = a + "\n"
                      c = re.sub("\n", "", i)
                      #a = a + "\n"
                      d = re.sub("\n", "", str(docno[a]))
                      b = c+" "+"0"+" "+str(d)+" "+str(k)+" "+str(Score_Comp[i][k][j+1])+" "+"BM25"+"\n"
                      fOutput.write(b)  

                                            
def process_query():
    fInput = open("files\\queryfile.txt")
    fOutput= open("files\\pro_query.txt", "w")
    query = fInput.readlines()
    for q in range(0, len(query)):
      #if q.find("<num>")>=0 or q.find("<title>")>=0:
       if query[q].find("<desc>")>= 0 or query[q].find("<num>")>=0:
       # stemWords = nltk.PorterStemmer()
        fOutput.write(query[q]+"\n"+query[q+1]+"\n")  

def process_query_2():
    fInput = open("files\\pro_query.txt")
    fOutput = open("files\\pre_query.txt", "w")
    query = fInput.read()
    query = re.sub("&blank", " ", query)
    query = re.sub("&hyph", "-", str(query))
    query = re.sub(";","", str(query))
    query = re.sub("/",'\n', query)
    query = re.sub("<[^>]*>", '', str(query))
    query = re.sub("Nubmer:", '', str(query))
    query = re.sub("Description:", '', str(query))
    query = re.sub("\n\n", "", str(query))
    #query = re.sub("\\", "\n", str(query))
    query = query.lower()
    query = query.split(" ")
    for q in query:
      if q!="" and q!="number:" and q!="topic:":
        fOutput.write(str(q)+"\n") 
def nsw_query():
     fInput = open("files\\pre_query.txt")
     fstops = open("files\\stops.txt")
     fOutput = open("files\\nsw_query.txt", "w")
     stops = fstops.readlines()
     lines = fInput.readlines()
     for line in lines:
         punc = re.match("\W", line)
         if not line in stops:
            if not punc:
             fOutput.write(line)         
start = time.clock()        
#test()
#term()
#cal_stem()
#cal_pos()
#cal_phrase()
new_index()
process_query()
process_query_2()
nsw_query()
tf_idf_term()
Score_BM25()
end = time.clock()
print end - start