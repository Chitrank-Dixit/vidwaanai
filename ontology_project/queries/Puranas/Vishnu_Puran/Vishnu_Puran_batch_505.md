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

### Verse 1 (Vishnu Puran 0.10081)
- **Original**: 22 हंसकुन्देन्दुधवल्ं. नीलाम्बरधरं. द्विज । तस्थानु बलभद्र च दर्दर्श यदुनन्दनम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10082)
- **Original**: 23 प्रांशुमुत्तुइ्॒याह्ंस विकासिमुखपड्डजम । मेघमालापरिवृतं. कैल्शासाद्रिमिबापरम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10083)
- **Original**: 24 तौ दृष्ठा बिकसद्क्त्सरोज: स महामतिः । पुलकाश्चितसर्वाड्रस्तदाक़ूरोउभवन्मुने.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10084)
- **Original**: 25 तदेतत्पर्मं धाम तदेतत्परर्ण पदम्‌ । भगवद्गासुदेवांशो द्विधा यो5यं व्यवस्थित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10085)
- **Original**: 26 साफल्यमक्ष्णोर्युगमेतदत्र दृष्टे जगद्धातरि यातमुच्चेः । डन मायापतिको बलारम्बार नमस्कार है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10086)
- **Original**: जिनमें हृदयकों लगा देनेसे पुए्ष इस योगमायारूप विस्तृत अखिद्याको पार कर जाता है, उन विद्यास्वरूप श्रोहस्को नमक्‍हकार है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10087)
- **Original**: जिन्हें याज्ञिकलोग 'यज्ञपुरुष', सात्वत (यादव अथवा भगवद्धक्त) गण 'वासुदेव' और वेदान्तयेत्ता 'विष्णु' कहते हैं उन्हें बारम्बार नमस्कार है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10088)
- **Original**: जिस (सल्य) से यह सदसद्गुप जगत्‌ उस जगदाधार विधातामें ही स्थित है ठस सत्ययलसे ही वे प्रभु मुझपर प्रसन्न हों
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10089)
- **Original**: जिनके स्मरणमात्रसे पुरुष सर्वथा कल्याणपात्र हो जाता है, मैं सर्वदा उन अजन्मा हरिकी दारणमें प्राप्त होता हूँ”
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10090)
- **Original**: श्रीपराह्रजी ओख्े--हे मैन्नेय ! भक्तिविनग्रक्षित्त अक्रूरजी इस प्रकार श्रीविष्णुभगवानका चित्तन करते कुछ-कुछ सूर्य रहते ही गोकुलमें पहुँच गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10091)
- **Original**: बहाँ पहुँचनेपर पहले उन्होंने खिले हुए गीलकमलकी-सी कान्तिवाले.श्रीकृष्णचन्द्रको गौओंके दोहनस्थाममें कछड़ोंके जीच विराजमान देखा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10092)
- **Original**: जिनके नेत्र जिसके हुए कमरूके समान थे, वक्षःस्थलमें श्रोचत्स-चिह्न सुजञोभित था, भुजाएँ लम्बी-लम्बी थीं, वक्ष/स्थछ विश्ञारू और ऊँचा था तथा नासिका उन्नत थी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10093)
- **Original**: जो सविलास हासयूक्त मनोहर मुखारविन्दसे सुशोभित थे तथा उन्नत और रक्तनखयुक्त चरणोंसे पृथिवीपर विराजमान थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10094)
- **Original**: जो दो पीताम्बर धारण किये थे, कन्यपुष्पोंसे विभूषित थे तथा जिनका श्वेत कमलूके आभूषणोंसे युक्त इयाम शरीर सचन्द्र जील्माचलके समान सुशोभित था
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10095)
- **Original**: हे द्विज
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10096)
- **Original**: श्रोव्रजचद्के पीछे उन्होंने हस, कुन्द और चनद्रमाके समान गौरवर्ण नौलाम्बरघारी यदुनन्दन श्रीबलूभद्रजीको देखा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10097)
- **Original**: खिज्लारू भुजदण्ड, उन्नत स्क-ध और विकसित-मुखारचिन्द श्रीबकूभद्रजी मेघमालासे घिरे हुए दूसरे कैलासपर्वतके समान जान पड़ते थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10098)
- **Original**: हे मुने ! उन दोनों बालकॉको देखकर महामति अक्रूरजीका मुखकमल प्रफुल्लित हो गया तथा डनके सर्वाज्जमें पुकक्तावली छा गयी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10099)
- **Original**: [ और वे मन-ही-मन कहने त्मों-- ] इन दो रूपोंमें जो यह भगवान्‌ वासुदेवका औद्य स्थित है वही परमधाम है और वही परमपद है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10100)
- **Original**: इन जगद्ठिधाताके दर्शन पाकर आज मेरे नेत्रयुगल तो सफल हो गये; किंतु क्या अब
- **Translation**: 

---

