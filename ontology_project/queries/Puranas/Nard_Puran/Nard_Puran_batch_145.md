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

### Verse 1 (Nard Puran 224.2881)
- **Original**: दीर्घ माना गया है और “ल' का अर्थ है। मुने! जिसमें तीनों अक्षर लघु हों, वह नगण
- **Translation**: 

---

### Verse 2 (Nard Puran 224.2882)
- **Original**: लघु समझा जाता है। पद्ध या श्लोकके एक (
- **Translation**: 

---

### Verse 3 (Nard Puran 224.2883)
- **Original**: ।) कहा गया है। तीन अक्षरोंके समुदायका
- **Translation**: 

---

### Verse 4 (Nard Puran 224.2884)
- **Original**: चौथाई भागकों पाद कहते हैं। विच्छेद या नाम गण है'
- **Translation**: 

---

### Verse 5 (Nard Puran 224.2885)
- **Original**: आर्या आदि छन्दोंमें चार
- **Translation**: 

---

### Verse 6 (Nard Puran 224.2886)
- **Original**: विरामका नाम “यति' है
- **Translation**: 

---

### Verse 7 (Nard Puran 224.2887)
- **Original**: नारद! वृत्त मात्रावाले पाँच गण कहे गये हैं, जो चार
- **Translation**: 

---

### Verse 8 (Nard Puran 224.2888)
- **Original**: (छन्द)-के तीन भेद माने गये हैं-- सम वृत्त, लघुवाले गणसे युक्त हैं'। यदि लघु अक्षरसे
- **Translation**: 

---

### Verse 9 (Nard Puran 224.2889)
- **Original**: अर्धसम वृत्त तथा विषम वृत्त। जिसके चारों परे संयोग, विसर्ग और अनुस्वार हो तो
- **Translation**: 

---

### Verse 10 (Nard Puran 224.2890)
- **Original**: चरणोंमें समान लक्षण लक्षित होता हो, वह सम वह लघुकी दीर्घताका बोधक होता है'।
- **Translation**: 

---

### Verse 11 (Nard Puran 224.2891)
- **Original**: वृत्तों कहलाता है
- **Translation**: 

---

### Verse 12 (Nard Puran 224.2892)
- **Original**: जिसके प्रथम और इस हन्‍्दःशास्त्रमें '“ग' का अर्थ गुरु या
- **Translation**: 

---

### Verse 13 (Nard Puran 224.2893)
- **Original**: तीसरे चरणोंमें एवं दूसरे तथा चौथे चरणोंमें कि शिलय लिल ि क0 मित्र संझएँ यदि काव्यमें ऐसे छन्दकों चुना गया, जो जगण आदि अनिष्टकारी गणोंसे संयुक्त हो तो उसकी शान्तिके लिये प्रारम्भमें भगवद्धाचक एवं देवतावाचक शब्दोंका प्रयोग करना चाहिये; जैसा कि भामहका बचन है-- देवतावाचका: शब्द ये च भद्रादिवाचका:। ते सर्वे नैव निन्ध्या: स्पुरलिपितों गणतो5पि बा
- **Translation**: 

---

### Verse 14 (Nard Puran 224.2894)
- **Original**: (पिड्जनलसूत्रको हलायुध-वृत्तिसे उद्धृत) 'जो देवतावाचक और मड्भलादिवाचक शब्द हैं, वे सब लिपिदोष या गणदोषसे भी निन्दित नहीं होते।' (उनके द्वारा उक्त दोषोंका निवारण हो जाता है।) 2.यथा- . सर्वगुरु अन्त्यगुरु मध्यगुरु आदिगुरु. चत्तुर्लघु 55 5 5। 5 । हा 1 2 के है 5 इन भेदोंके नाम क्रमश: इस प्रकार है--कर्ण, करतल, पयोधर, वसुचरण और विष्ठ। 3. जैसे-रामं। राम:। रामस्य। यहाँ 'राम' शब्दके “म' में हस्व अकार है, तथापि उसमें अनुस्वार और विसर्गका सम्बन्ध होनेसे वह दीर्घ ही माना जाता है। इसी प्रकार 'स्य' यह संयुक्त अक्षर परे होनेसे 'रामस्य' में मकारके परबर्ती अकारको दीर्घ समझा जाता है। पादके अन्तमें जो लघु अक्षर हो, यह भी विकल्पसे 'गुरु' माना जाता है। 4. सम यृत्तका उदाहरण- मुखे ते ताम्बूलं नयनयुगले कजलकला ललाटे काश्मीर॑ विलसति गले मौक्तिकलता। स्फुरत्काञ्नी शाटी पृथुकटितटे हाटकमयी भजामि त्वां गौरी नगपतिकिशोरीमविरतम्‌
- **Translation**: 

---

### Verse 15 (Nard Puran 224.2895)
- **Original**: (इस 'शिखरिणी' छन्दके चारों चरणोंमें एक समान हस्व-दीर्घबाले सत्रह-सत्रह अक्षर हैं।)
- **Translation**: 

---

### Verse 16 (Nard Puran 224.2896)
- **Original**: 376 संक्षिप्त नारदपुराण समान लक्षण हों, वह अर्धसम' वृत्त है। जिसके
- **Translation**: 

---

### Verse 17 (Nard Puran 224.2897)
- **Original**: गाथा होती है। अब क्रमश: एकसे छब्बीस चारों चरणोंमें एक-दूसरेसे भिन्न लक्षण लक्षित
- **Translation**: 

---

### Verse 18 (Nard Puran 224.2898)
- **Original**: अक्षरतकके पादवाले छन्दोंकी संज्ञा सुनो
- **Translation**: 

---

### Verse 19 (Nard Puran 224.2899)
- **Original**: 9- होते हों, वह विषम' वृत्त है
- **Translation**: 

---

### Verse 20 (Nard Puran 224.2900)
- **Original**: उक्ता, अत्युक्ता, मध्या, प्रतिष्ठा, सुप्रतिष्ठा, अक्षरके पादसे आरम्भ करके एक-एक अक्षर
- **Translation**: 

---

