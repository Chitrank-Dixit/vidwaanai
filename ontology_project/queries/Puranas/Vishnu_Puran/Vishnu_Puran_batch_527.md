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

### Verse 1 (Vishnu Puran 0.10521)
- **Original**: 5 विलेपुर्मातरश्रास्य दुःखशोकपरिफ्ुता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10522)
- **Original**: 7 बहुप्रकारमत्यर्थ पश्चात्तापातुरो हरि: । तास्समाश्वासयामास स्वयमस्राविलेक्षण:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10523)
- **Original**: 8 उग्रसेने ततो बन्धात्मुमोच मधुसूदन: । अभ्यसिज्ञत्तदैवैनं निजराज्ये हतात्मजम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10524)
- **Original**: 9 राज्येडभिषिक्त: कृष्णेन यदुसिंहस्सुतस्य सः । चकार प्रेतकार्याणि ये चान्ये तत्र घातिता:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10525)
- **Original**: 10 कृतोर्द्धवदैहिक चैन॑ सिंहासनगत॑ हरिः । उवाचाज्ञापय विभो यत्कार्यमविशज्धितः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10526)
- **Original**: 19 ययातिशापादशो5यमराज्याहोंअपि. साम्प्रतम्‌ । मयि भृत्ये स्थिते देवानाज्ञापयतु कि नृषैः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10527)
- **Original**: 12 अपराशर उवाच इत्युक्त्वा सो3स्परद्यायुमाजगाम च् तत्क्षणात्‌ उबाच चैन भगवान्केशवः कार्यमानुष:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10528)
- **Original**: 13 श्रीपराइरजी बोले--अपने अति अद्भुत क्मोंको देखनेसे वसुदेव और देवकीक्ा विज्ञान उत्पन्न हुआ देखकर भगवानने यदुवैश्चियोँंकों मोहित करनेके छिये अपनी सैष्णवी मायाका विस्तार किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10529)
- **Original**: और बोले--''हे मातः ! है पिताजी ! बलरामजी और मैं बहुत दिनोंसे कंसके भयसे छिपे हुए आपके दर्शनोके लिये उत्काषण्ठत थे, सो आज आपका दर्डान हुआ है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10530)
- **Original**: जो समय माता-पिताकी सेवा किये बिना वीतता है बह असाघु पुरुषोंकी ही आयुका भाग व्यर्थ जाता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10531)
- **Original**: हे तात ! शुरु, देव, ब्राह्मण और माता-पिताका पूजन करते रहनेसे देहधारियोंका जीवन सफल हे जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10532)
- **Original**: अतः हे ज्ञात ! कंसके वीर्य और प्रतापसे भीत हम परवशोंसे जो कुछ अपराध हुआ हो वह क्षमा करें”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10533)
- **Original**: श्रीपराश्रजी बोलले--राम और कृष्णने इस प्रकार कह माता-पिताों प्रणाम किया और फिर क्रमशः समस्त यदुवृद्धोंका यथायोग्य अभिबादनकर पुरवासियोंका सम्मान किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10534)
- **Original**: उस समय कंसकी पत्रियाँ और माताएँ पृथिब्रीपर पड़े हुए मृतक कंसको मेरकर दुःख- शोकसे पूर्ण हो विलाप करने लगीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10535)
- **Original**: तब कृष्णचन्द्रने भी अत्यन्त पश्चातापसे विहल हो स्वर्य आँखोंमें आँसू भरकर उन्हें अनेकों प्रकारसे लाँठस नैधाया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10536)
- **Original**: तदनन्तर श्रीमधुसूदनने उम्रसेनको बन्धनसे मुक्त किया और पुत्रके मारे जानेपर उन्हें अपने ग़ज्यपदपर अभिषिक्त किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10537)
- **Original**: श्रीकृष्णचछद्वारा राज्याभिषिक्त होकर यदुश्रेष्ठ उमग्रसेनने अपने पुत्र तथा और भी जो लोग वहाँ मारे गये थे उन सबके ओऔर्वदैहिक कर्म किये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10538)
- **Original**: और्ध्वदेहिक करमोसे निद्तत्त होनेपर सिंहासनारूढ़ उग्रसेनसे श्रीहरि बोके--“हे विभो ! हमारे योग्य जो सेवा हो उसके लिये हमें निइशंक होकर आज़ा दीजिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10539)
- **Original**: ययातिका शाप होनेसे यद्यपि हमारा बंद राज्यका अधिकारी नहीं है तथापि इस समय मुझ दासके रहते हुए राजाओंको तो क्या, आप देवताऑको भी आज्ना दे सकते हें”
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10540)
- **Original**: श्रीपराशरजी बोल्ले--उम्रसेनसे इस प्रकार कह [धर्मस॑स्थापनादि
- **Translation**: 

---

