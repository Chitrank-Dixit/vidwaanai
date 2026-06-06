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

### Verse 1 (Vishnu Puran 0.9981)
- **Original**: तदनन्तर, मेरे बधकी इच्छावाले इन समस्त दुष्ट गोपोके सम्पूर्ण गोधन तथा घनको मैं छीन रूँगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9982)
- **Original**: हे दानपते ! आपके अतिरिक्त ये सभी यादवगण मुझसे देष करते हैं, अतः मैं क्रमदा: इन सभीको नष्ट करनेका प्रयन्ल करूँगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9983)
- **Original**: फिर मैं आपके साथ मिलकर इस यादवहीन राज्यको निर्विश्नतापूर्वक भोगुँगा, अतः हे वीर! मेरी प्रसन्नताके लिये आप झीम्र हो जाइये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9984)
- **Original**: आप गोकुलमें पहुँचकर गोपगणोंसे इस प्रकार कहें जिससे वे माहिष्य (भैंसके) घृत और दि आदि उपफ्हारोंके सहित जीघ्र ही यहाँ आ जाये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9985)
- **Original**: श्रीपराशरजी बोले-- हे द्विज ! कैससे ऐसी आज्ञा पा महाभागवत अक्ूरजी 'कल मैं शीघ्र ही श्रीकृष्णच-द्रको देखूँगा'--बह सोचकर अत्ति प्रसत्र हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9986)
- **Original**: माधव-प्रिय अक्रूरजी राजा क॑ससे 'जो आज्ञा' कह एक अति सुन्दर रथपर चढ़े और मथुरापुरीसे बाहर निकल निश्चक्राम ततः पुर्या मथुराया मथुप्रिय:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9987)
- **Original**: चलन औ फन्‍+- इति श्रीविष्णुपुराणे पञ्मेंडशे पद्लदशो5ध्याय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9988)
- **Original**: चनतत् फ् सतत
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9989)
- **Original**: 0 मे शजनकल कम ननजमिनन्सनिकज सनम सी शिलीनि........ 5... शनिनििििली जिन सी स जिसकी जन"... ] पश्चम अंदा 351 सोलहवबाँ अध्याय केशि-वघ अ्रीपराझर उवाच केशी चापि बलोदग्न: कंसदूतप्रचोदित: । कृष्णस्य निधनाकाड्ली वृन्दावनमुपागमत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9990)
- **Original**: 9 स॒ खुरक्षतभूपृष्ठस्सटाक्षेपधुताम्बुद: । छुतविक्रान्तचन्द्राकपा्गों गोपानुपाद्रबत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9991)
- **Original**: 2 तस्य हेषितशब्देन गोपाला दैत्यवाजिन: । गोष्यश्च भयसंविप्ना गोविन्द शरणं ययुः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9992)
- **Original**: 3 ज्राहि त्राहीति गोविन्द: श्रुत्वा तेषों ततो बच: । सतोयजलद॒ध्यानगम्भीरमिदमुक्ततान्‌ू_
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9993)
- **Original**: 4 अलंत्रासेन गोपाल्छा; केशिन: कि भयातुरैः । भ्रवद्धिगोपजातीयैबीरवीरय॑ विलोप्यते ।। 5 किमनेनाल्‍पसारेण हेषिताटोपकारिणा । दैतेयब्रलवाहोन वल्गता वुष्टवाजिना
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9994)
- **Original**: 6 एह्वोहि दुष्ट कृष्णो5ह पृष्णस्त्विव पिनाकधृक्‌ । पातयिष्याप्ति दशनान्वदनादखिलांस्तव
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9995)
- **Original**: 7 इत्युक्ववास्फोट्य गोविन्दः केशिनस्सम्मुर्ख ययौ । विवृतास्यश्च सो5प्येनं दैतेयाश्व उपाद्रवत्‌ ।। 8 बाहुमाभोगिन कृत्वा मुखे तस्य जनार्दन: । प्रवेशयामास तदा केशिनो दुष्टवाजिन:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9996)
- **Original**: 9 केशिनो बदने तेन विशता कृष्णबाहुना । शातिता दह्नाः पेतुः सिताभ्रावयवा डइब
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9997)
- **Original**: 10 कृष्णस्य ववृथे बाहु: केशिदेहगतो द्विज । बिनाश्ञाय यथा व्याधिरासम्यूतेरुपेक्षित:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9998)
- **Original**: 19 विपाटितोष्ठो बहुलं सफेन॑ रुधिरं वमन्‌। सो$क्षिणी विवृते चक्रे विशिष्टे मुक्तबन्धने
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9999)
- **Original**: 12 जघान धरणों पादैर्शकृन्पूत्र समुत्सृजन्‌। स्वेदाद्रगात्रइशान्तश्ष॒निर्यत्रस्सो$भकक्‍तदा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10000)
- **Original**: 13 श्रीपराशरजी बोले--हे मैत्रेय ! इधर कैसके दूतद्वारा भेजा हुआ महानली केशी भी कृष्णचन्द्रके वधकी इच्छासे [ शोड़ेका रूप धारणकर ] वुन्दावनमें आया
- **Translation**: 

---

