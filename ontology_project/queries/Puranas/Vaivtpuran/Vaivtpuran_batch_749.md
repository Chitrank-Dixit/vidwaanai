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

### Verse 1 (Vaivtpuran 543.13294)
- **Original**: तथा वसिष्ठजीकी धर्मपत्नीने मेरे घरमें पदार्पण करके प्रसन्नतापूर्वक् अपने घरका रास्ता लिया।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13295)
- **Original**: कियां है। देवि! मैं आपकी किड्धरी हूँ। यह ब्राह्मणकी पूर्वोक्त बात सुनकर मेना शोकयुक्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13296)
- **Original**: घर आपका है। हमारे बड़े पुण्यसे आपका यहाँ हो नेत्रोंसे आँसू बहाने लगीं। उनका हृदय व्यथित
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13297)
- **Original**: शुभागमन हुआ है। हो उठा। वे हिमालयसे बोलीं। सम्भ्रमपूर्वक इतना ही कहकर मेनाने सती मेनाने कहा--शैलराज! मेरी बात सुनिये,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13298)
- **Original**: अरुन्धतीको सोनेकी चौकीपर बिठाया और उनके जो परिणाममें सुख देनेवाली है। आप इन श्रेष्ठ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13299)
- **Original**: चरण पखारकर उन्हें मिष्टान्न भोजन कराया। फिर पर्वतोंसे पूछिये, इनकी क्या राय है। मैं तो अपनी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13300)
- **Original**: स्वयं भी पुत्रीके साथ भोजन किया। तदनन्तर बेटीको शंकरके हाथमें नहीं दूँगो। देखिये, मैं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13301)
- **Original**: अरुन्‍्धतीने मेनाको शिवके लिये नीतिकी बातें सारे विषयोंको त्याग दूँगी, विष खा लूँगी और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13302)
- **Original**: समझायीं और प्रसज्ग़वश उनके साथ सम्बन्ध पार्वतीके गलेमें फाँसी लगाकर भयानक बनमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13303)
- **Original**: जोड़नेवाले वचन भी कहे। इधर उन महर्पियोंने चली जाऊँगी। भी शैलराजको उत्तम वाणीमें नीतिका सारतत्त्व ऐसा कह मेना रोषपूर्वक पार्वतीका हाथ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13304)
- **Original**: समझाया और प्रसड्भवश ऐसी बातें कहीं, जो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13305)
- **Original**: + श्रीकृष्णजन्मखण्ड « 579 शिव और पार्वतीके सम्बन्धकों जोड़नेवाली थीं। वसिष्ठजीने कहा--शैलराज! लोक और ऋषि बोले--शैलराज ! हमारी बात सुनो।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13306)
- **Original**: वेदमें तीन प्रकार के वचन कहे गये हैं। शास्त्रज् यह तुम्हारे लिये शुभकारक है। तुम पार्वतीका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13307)
- **Original**: पुरुष अपनी निर्मल ज्ञानदृष्टिसे उन सभी बचनोंको विवाह शिवके साथ कर दो और उन लोकसंहारक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13308)
- **Original**: जानता है। पहला वचन वह है, जो वर्तमान महादेवके श्वशुर बनो। देवेश्वर शिव तुमसे याचना
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13309)
- **Original**: कालमें कानॉंको सुन्दर लगे और जल्दी समझमें नहीं करेंगे। तुम यत्रपूर्वक शीघ्र ही उन्हें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13310)
- **Original**: आ जाय; किंतु पीछे असत्य और अहितकर सिद्ध समझाओ-विवाहके लिये तैयार करो। तुम्हारी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13311)
- **Original**: हो। ऐसी बात केवल शत्रु कहता है। इससे शंकाका निवारण करनेके लिये ब्रह्माजी स्वयं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13312)
- **Original**: कदापि हित नहीं होता। दूसरे प्रकारका वचन वह विवाह स्थिर करानेके निमित्त प्रयत्न करें। योगियोंमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13313)
- **Original**: है, जो आरम्भमें सहसा दुःखजनक जान पड़े; श्रेष्ठ शंकर कभी विवाहके लिये इच्छुक नहीं हैं।
- **Translation**: 

---

