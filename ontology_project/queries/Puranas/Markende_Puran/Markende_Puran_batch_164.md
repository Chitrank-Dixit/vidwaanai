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

### Verse 1 (Markende Puran 0.3261)
- **Original**: कचूमर निकल गयया
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3262)
- **Original**: वैष्णवीने भी अपने महापशक्रमो पुरुष 'खड़ी रह, खड़ी रह' कहता हुआ अक्रसे द्वानवॉके टुकद़्े-टुकडे कर डाले। ऐद्रीके निकला
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3263)
- **Original**: उस निकलते हुए पुरुषकी बात
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3264)
- **Original**: हाथसे छूटे हुए तनज़से भी कितने ही प्राणोंसे हाथ सुनकर देबी ठठाकर हँस पड़ी और खड्गसें उन्होंने
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3265)
- **Original**: धो बैठे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3266)
- **Original**: कुछ अखुर नष्ट हो गये, कुछ उस उम्तका मस्तक काट डाला। फिर तो वह पृश्लोपर सहासुद्से भाग गये तथा कितने ही काली, शिवदूती गिर पड़ा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3267)
- **Original**: त्तदगत्तर सिंह अपनी दाढ़ोंसे असुरोंकी
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3268)
- **Original**: तथा सिंहके ग्रास बन गये
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3269)
- **Original**: श॒त्ति ऑमार्फण्डेण्पुएणे साकतिके म्यस्तों वेकोफाहातों विशुस्भवायों व तफणोंठ ध्याव:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3270)
- **Original**: 9 # उकाच 2. रतोोब्य: 79, छुलएू 46, शृक्‍फदित: 45434 इस प्रकार श्रीप्रार्कण्डेयपुराणपें साधर्ष्णिक पन्वन्तरकी कथाके अन्तर्गत देवीमाहात्म्यमें 'निशुष्भ-बध' नामक्त नत्राँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3271)
- **Original**: 2077 आओ ।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3272)
- **Original**: कं -खधघ «< 5 $ 30 कब सजा जऋ 41 7077 54445 544 4722 22023 27747777 86:46 222.2002 2.7 79777 0 7 7 #4 5 4:8702:32:/0 0777 +क्& दरशशमो5ध्याय: शुम्भ-वध श्यान ये मेरी ही विभृतियाँ हैं, अत: मुझमें हो प्रवेश (*337' उन्तमहेमरुचिरां रदिचखयहि- कर रहो हैं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3273)
- **Original**: नेत्रां. धनुशशर्युताज़ुशपाशशूलम्‌।
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3274)
- **Original**: ततः समस्तास्ता देव्यों च्रद्माणीप्रमुखा लयम्‌। रम्यैभुंजैश्ञ दधती . शिवशक्तिरूपां तस्था देव्यास्तनी जंग्मुरेकेयासीज्षदाम्बिका
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3275)
- **Original**: का्मेश्वरीं दृदि भजामि धृतेन्दुलेखाम
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3276)
- **Original**: तदनन्तर ज़ह्माणीं आदि समस्त देव्रियाँ अम्बिका मैं मस्तकपर अर्द्धचन्द्र धारण करनेचाली शिवशक्तिस्वरूपा भगवत्तीं कामेश्वरौका इृदकमों चिन्तन करता हूँ। ले तपाये हुए सूवर्णफे समान ध्ुन्दर हैं। सूर्य, चन्द्रपा और अग्नि--बे हीं तीन उनके नेत्र हैं तथा बे अपने मनोहर हाथोंमें धनुष-बाण, अक्कूश, पाश और शुल धारण किवे हुए हैं।) ऋषित्वाक्ष
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3277)
- **Original**: € # *3& 'निशुम्भे निहर्त दृष्ठा भ्रातरे प्राणसम्मितम्‌। हन्यमान॑ जल॑ चअऔैश शुम्भ: क़ुद्धोउल्नवीद्नच्न:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3278)
- **Original**: अलावलेपाहु्टे' त्व॑ मा दुर्गे गर्धपावह। अन्यासा बलमाश्रित्य युद्धएसे यातिमातरिनी
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3279)
- **Original**: 3 ऋषि कहते हैं--
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3280)
- **Original**: राजन्‌ ! अपने प्राणोके समान प्यारे भाई दिशु+भकों मारा गया देख तथा सारी येनाका संहार होता जात शुम्भने कुपित होकर कहा--
- **Translation**: 

---

