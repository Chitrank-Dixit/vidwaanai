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

### Verse 1 (Bhagwat_Geeta 1.121)
- **Original**: येषामर्थ काद्धिश्षतं नो राज्यं भोगा: सुखानि च। त इमे5वस्थिता युद्धे प्राणांस्त्यक्त्वा धनानि च
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 1.122)
- **Original**: हमें जिनके लिये राज्य, भोग और सुखादि अभीष्ट हैं, वे ही ये सब धन और जीवनकी आशाको त्यागकर युद्धमें खड़े हैं
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 1.123)
- **Original**: आचार्या: पितरः पुत्रास्तथेव च पितामहा: । मातुला: श्रशुरा: पौत्रा: एयाला: सम्बन्धिनस्तथा।
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 1.124)
- **Original**: । गुरुजन, ताऊ-चाचे, लड़के और उसी प्रकार दादे, मामे, ससुर, पौत्र, साले तथा और भी सम्बन्धी लोग हैं
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 1.125)
- **Original**: एतान्न हन्तुमिच्छामि घ्नतोडपि मधुसूदन। अपि त्रैलोक्यराज्यस्य हेतो: कि नु महीकृते
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 1.126)
- **Original**: हे मधुसूदन ! मुझे मारनेपर भी अथवा तीनों लोकोंके राज्यके लिये भी मैं इन सबको मारना नहीं चाहता; फिर पृथ्वीके लिये तो कहना ही क्‍या है 2
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 1.127)
- **Original**: निहत्य धार्तराष्ट्रान्न: का प्रीति: स्याज्जनार्दन। पापमेवा श्रयेदस्मान्हत्वैतानाततायिन: .
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 1.128)
- **Original**: हे जनार्दन! धृतराष्ट्रके पुत्रोंको मारकर हमें क्या
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 1.129)
- **Original**: 22 * श्रीमद्धगवद्रीता * प्रसन्‍नता होगी ? इन आततायियोंको मारकर तो हमें पाप ही लगेगा
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 1.130)
- **Original**: तस्मान्नार्हा वयं हन्तुं धार्तराष्ट्रान्स्वबान्धवान्‌ । स्वजनं हि कथं हत्वा सुखिनः स्यथाम माधव
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 1.131)
- **Original**: अतएव हे माधव! अपने ही बान्धव धृतराष्ट्रके पुत्रोंको मारनेके लिये हम योग्य नहीं हैं; क्योंकि अपने ही कुट॒म्बको मारकर हम कैसे सुखी होंगे 2
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 1.132)
- **Original**: यह्यप्येते न पश्यन्ति लोभोपहतचेतसः । कुलक्षयकृतं दोषं मित्रद्रोहे च॒ पातकम्‌
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 1.133)
- **Original**: कथ॑ं न ज्ञेयमस्माभि: पापादस्मान्निवर्तितुम्‌। कुलक्षयकृतं दोषं प्रपश्यद्धिर्जनार्दन
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 1.134)
- **Original**: यद्यपि लोभसे भ्रष्टचित्त हुए ये लोग कुलके नाशसे उत्पन्न दोषको और मित्रोंसे विरोध करनेमें पापको नहीं देखते, तो भी हे जनार्दन ! कुलके नाशसे उत्पन्न दोषको जाननेवाले हमलोगोंको इस पापसे हटनेके लिये क्‍यों नहीं विचार करना चाहिये 2
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 1.135)
- **Original**: कुलक्षये प्रणश्यन्ति कुलधर्मा: सनातना: । धर्मे नष्टे कुलं कृत्स्रमधर्मोडभिभवत्युत
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 1.136)
- **Original**: कुलके नाशसे सनातन कुल-धर्म नष्ट हो जाते हैं, धर्मके नाश हो जानेपर सम्पूर्ण कुलमें पाप भी बहुत फैल जाता है
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 1.137)
- **Original**: * अध्याय 1*% 23 अधर्माभिभवात्कृष्ण प्रदुष्यन्ति कुलस्त्रिय: । स्त्रीषु दुष्टासु वाष्णेय जायते वर्णसड्डूरः
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 1.138)
- **Original**: हे कृष्ण
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 1.139)
- **Original**: ! पापके अधिक बढ़ जानेसे कुलकी स्त्रियाँ अत्यन्त दूषित हो जाती हैं और हे वार्ष्णेय ! स्त्रियोंके दूषित हो जानेपर वर्णसंकर उत्पन्न होता है
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 1.140)
- **Original**: सड्जूरो नरकायैव कुलप्लानां कुलस्य च। पतन्ति पितरो होषां लुप्तपिण्डोदकक्रिया:
- **Translation**: 

---

