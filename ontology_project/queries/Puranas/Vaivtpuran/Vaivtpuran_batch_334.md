# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 16.907)
- **Original**: बासी पानीसे रूखा सत्रान (बिना तेल लगाये कारणों तथा उपायोंकों मुझसे सुनों। जब भूखकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.908)
- **Original**: नहाना), तरबूजके पके फल खाना, ककड़ीके आग प्रज्वलित हो रही हो और उस समय आहार
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.909)
- **Original**: अधिक पके हुए फलका सेवन करना, वर्षा- न मिले तो प्राणियोंके शरीरमें--मणिपूरक' चक्रमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.910)
- **Original**: ऋतुमें तालाबमें नहाना और मूली खाना-इन पित्तका प्रकोप होता है। ताड़ और बेलका फल सबसे कफकी वृद्धि होती है। वह कफ ब्रह्मरम्भ्रमें अल कट लक तत्काल जल पी लिया जाय तो बही
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.911)
- **Original**: उत्पन्न होता है, जो महान्‌ वीर्यनाशक माना गया सद्यः प्राणनाशक पित्त हो जाता है। जो दैवका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.912)
- **Original**: है। गन्धर्वनन्दिनि! आग तापकर शरीरसे पसीना मारा हुआ पुरुष शरद-ऋतुमें गरम पानी पीता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.913)
- **Original**: निकालना, भूजी भाँगका सेवन करना, पकाये और भादोंमें तिक्त भोजन करता है, उसका पित्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.914)
- **Original**: हुए तेल-विशेषको काममें लाना, घूमना, सूखे बढ़ जाता है। धनिया पीसकर उसे शक्वरके साथ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.915)
- **Original**: पदार्थ खाना, सूखी पकी हरैंका सेबन करना, ठंडे जलमें घोल दिया जाय तो उसको पौनेसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.916)
- **Original**: कच्चा पिण्डारक' (पिण्डारा), कच्चा केला, पित्तकी शान्ति होती है। चना सब प्रकारका, गव्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.917)
- **Original**: बेसवार (पीसा हुआ जीरा, मिर्च, लौंग आदि * परापेन जायते व्याधिं: पापेन जायते जरा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.918)
- **Original**: पापेन जायते दैन्यं दुःखं शोकों भयंकर:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.919)
- **Original**: तस्मातू. पाप महावैरं. दोषबीजममज़लम्‌ । भार्ते संततं सन्‍्तो नाचरन्ति भयातुरा:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.920)
- **Original**: (ब्रह्मखण्ड 16। 51-52) 1. तन्त्रके अनुसार छः चक्रॉमेंसे तीसरा चक्र, जिसको स्थिति नाभिके पास मानी जाती है। यह तेजोमय और विद्युतके समान आभावाला है। इसका रंग नीला है। इसमें दस दल होते हैं और उन अक्षरोंपर 'ड' से लेकर “फ' तकके अक्षर अंकित हैं। वह चक्र शिवका निवासस्थान माना जाता है। उसपर ध्यान लगानेसे सब विषयोंका ज्ञान हो जाता है। 2. एक प्रकारका फल-शाक। 3. एक जड़ीका पौधा। भावप्रकाशके अनुसार यह पौधा हिमालयके शिखरोंपर होता है। इसका कन्द लहसुनके कन्दके समान और इसकी पत्तियाँ महीन सारहीन होतो हैं। इसकौ टहनियोंमें बारीक काँटे होते हैं और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.921)
- **Original**: + ब्रह्मखए्ड +» ड7 अऊकड ऊ 44 ऋ 4 5 ऋ 4 ऋ# 4 % 45 4548 4 4544 #5$88# 94 859 # 4 # 54 ## ## $ 844 # 6 6# 56 # ## 6 5 5 5 4 % $ 4 5 ह 5 5 # मसाला), सिन्धुवार (सिन्दुबार या निगुंडी),
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.922)
- **Original**: क्लेशजनित, मानसिक संतापजनित और कामजनित। अनाहार (उपवास), अपानक (पानी न पीना),
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.923)
- **Original**: मालावति! इस प्रकार मैंने तुम्हारे समक्ष घृतमिश्रित रोचना-चूर्ण, घी मिलाया हुआ सूखा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.924)
- **Original**: रोगसमूहका वर्णन किया तथा उन रोगोंके शक्कर, काली मिर्च, पिप्पल, सूखा अदरक,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.925)
- **Original**: नाशके लिये श्रेष्ठ विद्वानोंने जो नाना प्रकारके जीवक (अष्टवर्गान्तर्गत औषधविशेष) तथा मधु-ये
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.926)
- **Original**: तनत्र बनाये हैं, उनकी भी चर्चा की। बे सभी द्रव्य तत्काल कफको दूर करनेवाले तथा बल
- **Translation**: 

---

