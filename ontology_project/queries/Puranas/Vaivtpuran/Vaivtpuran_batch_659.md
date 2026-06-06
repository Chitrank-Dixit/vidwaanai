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

### Verse 1 (Vaivtpuran 67.5975)
- **Original**: अनेकविध व्यञ्ञन थे। देवर्षिगणोंके साथ स्वयं रत्रोंके उद्धवस्थान हैं, कौतुकबश अपनी कन्याके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5976)
- **Original**: नारायणने भोजन किया। उस समय एक लाख ब्रतमें रल्ाभरणोंसे अलंकृत हो पत्नी, पुत्र, गण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5977)
- **Original**: ब्राह्मण परोसनेका काम कर रहे थे। (भोजन और अनुयायियॉसहित पधारे। उनके साथ नाना
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5978)
- **Original**: कर लेनेके पश्चात्‌) जब वे रज्नसिंहासनोंपर प्रकारके द्रव्योंसे संयुक्त बहुत बड़ी सामग्री थी।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5979)
- **Original**: विराजमान हुए, तब परम चतुर लाखों ब्राह्मणोंने उसमें ब्रतोपयोगी मणि-माणिक्य और रत्र थे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.5980)
- **Original**: उन्हें कर्पूर आदिसे सुवासित पानके बीड़े समर्पित अनेक प्रकारकी ऐसी वस्तुएँ थीं, जो संसारमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.5981)
- **Original**: किये। ब्रह्मन्‌! देवर्षियोंसे भरी हुई उस सभामें दुर्लभ हैं। एक लाख गज-रत्र, तीन लाख अश्व-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.5982)
- **Original**: जब क्षीरसागरशायी भगवान्‌ विष्णु रत्नसिंहासनपर रत्न, दस लाख गो-रत्र, एक करोड़ स्वर्णमुद्राएँ, आसीन थे, प्रसन्न मुखवाले पार्षद उनपर श्वेत चार लाख मुंक्ता, एक सहस्न कौस्तुभभण और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.5983)
- **Original**: चँवर डुला रहे थे, ऋषि, सिद्ध तथा देवगण अत्यन्त स्वादिष्ट तथा मीठे पदार्थॉक एक लाख
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.5984)
- **Original**: उनकी स्तुति कर रहे थे, वे गन्धर्वोंके मनोहर भार थे। इसके अतिरिक्त पार्वतीके ब्रतमें ब्राह्मण,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.5985)
- **Original**: गीत सुन रहे थे, उसी समय ब्रह्माको प्रेरणासे मनु, सिद्ध, नाग और विद्याधरोंके समुदाय तथा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.5986)
- **Original**: शंकरजीने हाथ जोड़कर भक्तिपूर्वक उन ब्रह्मेशसे संन्‍्यासी, भिक्षुक और बंदीगण भी आये। उस
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.5987)
- **Original**: अपने अभीष्ट कर्तव्य ब्रतके विषयमें प्रश्न किया। समय कैलासपर्वतके राजमार्गोपर चन्दनको श्रीमहादेवजीने पूछा--प्रभो! आप श्रीनिवास, छिड़काव किया गया था। पद्मरागमणिके बने हुए
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.5988)
- **Original**: तपःस्वरूप, तपस्याओं और कर्मोंके फलदाता, शिवमन्दिरमें आमके पल्लबोंकी बंदनवारें बँधी सबके द्वारा पूजित, सम्पूर्ण व्रतों, जप-यज्ञों और थीं। कदलीके खंभे उसकी शोभा बढ़ा रहे थे।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.5989)
- **Original**: पूजनोंके बीजरूपसे वाञ्छाकल्पतरु और पाषोंका वह दूब, धान्य, पत्ते, खील, फल और पुष्पोंसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.5990)
- **Original**: हरण करनेवाले हैं। नाथ! मेरी एक प्रार्थना
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.5991)
- **Original**: 302 * संक्षिप्त ब्रह्मवैवर्तपुराण * कक 6 ##############$%%%%%5$%$$%%%%%5%% 5; ######### 55% सुनिये। ब्रह्मन्‌! पुत्रशोकसे पीड़ित हुई पार्वतीका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.5992)
- **Original**: हैं, महान्‌ विराट्‌ जिनका एक अंश है, जो हृदय दुःखी हो गया है, अत: वह पुत्रको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5993)
- **Original**: निर्लिप्त, प्रकृतिसे परे, अविनाशी, निग्रहकर्ता, कामनासे परमोत्तम पुण्यक-त्रत करना चाहती है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5994)
- **Original**: उग्रस्वरूप, भक्तोंके लिये मूर्तिमान्‌ अनुग्रहस्वरूप, वह सु्रता ब्रतके फलस्वरूपमें उत्तम पुत्र और ग्रहोंमें उग्र ग्रह और ग्रहोंका निग्रह करनेवाले पति-सौभाग्यकी याचना कर रही है। इनके बिना
- **Translation**: 

---

