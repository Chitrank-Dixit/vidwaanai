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

### Verse 1 (Markende Puran 0.3361)
- **Original**: गुण्पाश्नबे गुणमणे नारामणि नम्तोउस्तु ते
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3362)
- **Original**: कात्यायनों तुष्टचुरिप्टलाभाद्‌ँ शरणागतंदीनात्तपरित्राणपरायणोें । बिक्राशिवक्त्राब्जचिकाशिताशा;
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3363)
- **Original**: सर्वस्यार्िहरे देति नारायणि नमोस्तु ते
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3364)
- **Original**: देखि प्रपन्नार्निहरे प्रसीद ' हँसयुक्तत्रिमानस्थे.. ब्रद्माणीरूपथारिणि। प्रसीद मात्तर्जगतो उखिलस्य। कौशाम्भ:क्षरिके देवि नारायण नमोस्तु ते
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3365)
- **Original**: प्रसीद विश्वेश्विा पाहि. विश बिशूलचन्द्राहिधरे महांवृषभवाहिनि। त्वभीश्वरी देशि चंराचरस्थ
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3366)
- **Original**: , माहेश्नरीस्वरूपेण नारायण नमों5स्तु ते
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3367)
- **Original**: आधारभूता जगतस्त्वमेक़ा मयूरक्रुक्कुटवृते महाशक्तिधरेउनघे । महीसस्‍्लरूपेण बतः स्थितासि। कौमारीरूपसंस्थाने ताग्रयण्ि नमोंउस्तु ते
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3368)
- **Original**: अपो स्वरूपस्थितवमा त्वबैत- शब्भुचक्रगदाशाड़ूँगृहीतपरमायुथे । दाप्यासमते. कृत्समलछ्द्नवीर्ये
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3369)
- **Original**: प्रसीद वैष्णवीरूपे नागयणि नप्रोउस्तु ले
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3370)
- **Original**: क्वयं.. वैष्णवी शक्तिरनन्तवीर्या गुद्ीत़ोग्रपहाचक्रे उंष्टोद्धुतवसुंधरे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3371)
- **Original**: विश्वस्थ बीज परमासि माया। बराहरूपिणि शिवे नाराचणि नमोस्तु ते
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3372)
- **Original**: सम्मोहितं देवि ससमस्तमेतत्‌ नृर्तिहरूपेणोग्रेण हन्तुं दैत्यान्‌ कृतोंद्यमे। त्व॑ मै प्रसत्ना भुवि पुक्तिहेतु:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3373)
- **Original**: ज्रैलोक्यत्राणसहिते नारायण नमोस्तु ते
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3374)
- **Original**: विद्या: समस्तास्तव॒ देति. भेदाः किरीटिनि महावज़े सहस्वनयनोज्ल्लले। स्त्रियः समस्ता: सकला जगत्सु। चृत्रप्राणहरे चन्द्रि नाराग्रणि नमो5स्तु ते
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3375)
- **Original**: 2. पा0/लाभा0। 2. णर-वज्त/2 थिंएख। 3 झ0«-भुक्ति। 4. णर-साढ्नल्ये।
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3376)
- **Original**: >डैवताआद्वारा देशीकी स्तुति देवॉद्वारा देवताओंकों यरदान+ रइ्1 अं 5220:24:22:11700क भक4 # 555 22722 00477 # 8825. 23507 ++ कफ अा॒ अत लकू 4 56:552205%:5 4 77
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3377)
- **Original**: महज 22.2 फू ऊ ऊ शिवदूतीस्वरूपेण हतदैत्यमहावले। चोररूऐ महाराघे नाराबणि नप्रोउस्तु ते
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3378)
- **Original**: दंष्टाकरालबदने... शिरोमालाविभूषणे। आमुण्डे मुण्डमश्ने नाराबणि नमोउस्तु ते
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3379)
- **Original**: 2614 लक्ष्म सज्जे महाविद्ये श्रद्धे पुष्टिस्वेधे ध्रुते। महारात्रि' महा5विद्येरे नाधबणि नमोस्तु ते
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3380)
- **Original**: मेथे सरस्तति करे भूति बाभ्नत्रि तामासि। चियते त्वं प्रसीदेशे चारायणि नमोउस्सु ते
- **Translation**: 

---

