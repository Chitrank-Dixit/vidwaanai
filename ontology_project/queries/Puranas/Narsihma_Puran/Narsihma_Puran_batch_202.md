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

### Verse 1 (Narsihma Puran 0.4021)
- **Original**: राजन्‌! उनके इस प्रकार कहनेपर, विछयात पराक्रमो वीर हनुमानजी हाथ जोड़कर बोले--' देव ! आज्ञा दें, मैँ सेवामें उपस्थित हूँ'
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.4022)
- **Original**: ओऔरामने कहा--' महावोर! मुझे 'विशल्यकरणो' ओषधि चाहिये। सहायलों! उसे लाकर मेरे भाईकों शीघ्र हो नौरोग करो
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.4023)
- **Original**: तब हनुमानूजी बड़े वेगसे डछले और द्रोणगिरिपर जाकर शीघ्र ही यहाँसे दवा बाँधकर ले आये और उसका प्रयोग करके देवदेवेश्वरों तथा रामचन्द्रजीके देखते-देखते क्षणभरमें लक्ष्मणकों नीरोग कर दिया
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4024)
- **Original**: तदनन्तर जगदी भ्रर कमलनयन श्रोराम यहुत हो कुपित हुए और रावणकीं बची हुई सेनाकों हाथी, घोड़े, रथ तथा राक्षसोंसहित क्षणभरपें मार गिराया। उच्होंने तोखे बाणोंसे राबणका शरीर जजंर कर दिया और रणभृपिमें वानरोंसे घिरे हुए खड़े रहे। रावण निश्ले"्ट होकर गिर पड़ा। फिर धोरे- धीरे होशर्मे आनेपर बह उठकर कुपित हो सिंहनाद करने लगा। उसको गर्जना सुनकर आफाशवर्तो देवतालोग दहल गये
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.4025)
- **Original**: 14--26862/,
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.4026)
- **Original**: समय राखणके प्रति बाँध इसी चैर एतस्मित्रेव काले तु राम॑ प्राप्य महापुनि:
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.4027)
- **Original**: महामृति. अगस्त्थ श्रीरामचन्द्रजीेके पास आये
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.4028)
- **Original**: 226 राबणें अ्रद्धवैरस्तु अगस्त्यो वै जयप्रदम्‌। आदित्यह॒दय॑ नाम मन्त्र प्रादाज्जयप्रदम्‌
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.4029)
- **Original**: 98 रामो5पि जप्त्वा तन्मन््रमगस्त्योक्त जयप्रदम्‌। तद्दत्तं वैष्णव॑ चापमतुल॑ सद्ुर्ण दृढ़म्‌
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.4030)
- **Original**: 99 पूजयित्वा तदादाय सज्यं कृत्वा पहावल:। सौवर्णपुद्स्तीक्ष्णैस्तु. शरैर्मर्मविदारणै:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.4031)
- **Original**: 100 युयुथे राक्षसेन्द्रेण रघुनाथ: प्रतापबान्‌। तयोस्तु युध्यतोस्तत्र भीमशक्त्योर्महामते
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.4032)
- **Original**: 101 परस्परविसृष्टस्तु व्योम्नि संबर््धतोइनल:। समुत्यथितो नृपश्रेष्ठ रामरावणयोर्युधि
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.4033)
- **Original**: 102 संगरे वर्तमाने तु रामो दाशरथिस्तदा। पदातिर्युयुध्े खीरो रामोउनुक्तपराक्रप:
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.4034)
- **Original**: 103 सहस्त्राश्चयुतं दिव्यं रथ मातलिमेव च। प्रेषयामास देवेन्रों महान्तं लोकविश्रुतम्‌
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.4035)
- **Original**: 104 रामस्त॑ रथमारुहा पृज्यमान: सुरोत्तमै:। मातल्युक्तोपदेशस्तु रामचन्द्र: प्रतापवान्‌
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.4036)
- **Original**: 105 ब्रह्मदत्तवरं दुष्ट ब्रह्मास्त्रेण दशाननम्‌। जधान वैरिणं क़ूरं रामदेव: प्रतापवान्‌
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.4037)
- **Original**: 106 रामेण निहते तत्र रावणे सगणे रिपौ। इन्द्राद्मा देवता: सर्वा: परस्परमथाब्रुबन्‌
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.4038)
- **Original**: 107 रामों भूत्वा हरिर्यस्मादस्मार्क बैरिणं रणे। अन्यैरबध्यपप्येने जघान युथधि रावणम्‌
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.4039)
- **Original**: 108 तस्मात्तं रामनामानपमनन्तमपराजितम्‌। पूजयामो5बतीर्यनमित्युकत्वा ते दिवौकस:
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.4040)
- **Original**: 109 नानावियानै: श्रीमद्धिरवतीय महीतले। रुद्रेनद्रबसुचन्द्राद्या विधातारं सनातनम्‌
- **Translation**: 

---

