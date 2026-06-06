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

### Verse 1 (Vaivtpuran 48.4654)
- **Original**: सम्पत्ति देनेवाली राजलक्ष्मी भी उन्हींकी अंशभूता श्रीकृष्णने मन्द-मन्द मुस्कराती हुई अपनी उन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 48.4655)
- **Original**: हैं। राजलक्ष्मीकी अंशभूता मर्त्यलक्ष्मी हैं, जो प्रियतमाको देखा। प्राणवल्लभापर दृष्टि पड़ते ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 48.4656)
- **Original**: गृहस्थोंके घर-घरमें वास करती हैं। वे ही विश्वकान्त श्रीकृष्ण मिलनके लिये उत्सुक हो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 48.4657)
- **Original**: शस्याधिष्ठातृदेवी तथा वे ही गृहदेवी हैं। स्वयं गये। परम मनोहर कान्तिवाले प्राणबल्लभको देखते
- **Translation**: 

---

### Verse 5 (Vaivtpuran 48.4658)
- **Original**: श्रीराधा श्रीकृष्णकी प्रियतमा हैं तथा श्रीकृष्णके ही श्रीराधा उनके सामने दौड़ी गयीं। महेश्वरि!
- **Translation**: 

---

### Verse 6 (Vaivtpuran 48.4659)
- **Original**: ही वक्ष:स्थलमें वास करती हैं। बे उन परमात्मा उन्होंने अपने प्राणागाममकों ओर धावन किया, [ श्रीकृष्णके प्राणॉंकी अधिष्ठात्री देवी हैं। इसीलिये पुराणवेत्ता महापुरुषोंने उनका 'राधा' पार्वति! ब्रह्मासे लेकर तृण अथवा कौटपर्यन्त यह सार्थक नाम निश्चित किया। राधा श्रीकृष्णकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 48.4660)
- **Original**: सम्पूर्ण जगत्‌ मिथ्या ही है। केवल त्रिगुणातीत आराधना करती हैं और श्रीकृष्ण श्रीराधाकी। वे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 48.4661)
- **Original**: परब्रह्म परमात्मा श्रीराधावल्लभ श्रीकृष्ण ही परम दोनों परस्पर आराध्य और आराधक हैं। संतोंका सत्य हैं; अतः तुम उन्होंकी आराधना करो # वे कथन है कि उनमें सभी दृष्टियोंसे पूर्णत: समता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 48.4662)
- **Original**: सबसे प्रधान, परमात्मा, परमेश्वर, सबके आदिकारण, है।* महेश्वरि! मेरे ईश्वर श्रीकृष्ण रासमें प्रियाजीके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 48.4663)
- **Original**: सर्वपूज्य, निरीह तथा प्रकृतिसे परे विराजमान हैं। धावनकर्मका स्मरण करते हैं, इसीलिये वे उन्हें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 48.4664)
- **Original**: उनका नित्यरूप स्वेच्छामय है। वे भक्तोंपर अनुग्रह *राधा' कहते हैं, ऐसा मेरा अनुमान है। दुर्ग! भक्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 48.4665)
- **Original**: करनेके लिये ही शरीर धारण करते हैं। श्रीकृष्णसे पुरुष 'रा' शब्दके उच्चारणमात्रसे परम दुर्लभ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 48.4666)
- **Original**: भिन्न जो दूसरे-दूसरे देवता हैं; उनका रूप प्राकृत मुक्तिको पा लेता है और 'धा' शब्दके उच्चारणसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 48.4667)
- **Original**: तत्त्वोंसे ही गठित है। श्रीराधा श्रीकृष्णको प्राणोंसे वह निश्चय ही श्रीहरिके चरणोंमें दौड़कर पहुँच
- **Translation**: 

---

### Verse 15 (Vaivtpuran 48.4668)
- **Original**: भी अधिक प्रिय हैं। वे परम सौभाग्यशालिनी हैं। जाता है।'रा' का अर्थ है 'पाना' और 'धा' का
- **Translation**: 

---

### Verse 16 (Vaivtpuran 48.4669)
- **Original**: वे मूलप्रकृति परमेश्वरी श्रीराधा महाविष्णुकी जननी अर्थ है 'निर्वाण' (मोक्ष) । भक्तजन उनसे निर्वाण-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 48.4670)
- **Original**: हैं। संत पुरुष मानिनी राधाका सदा सेवन करते मुक्ति पाता है, इसलिये उन्हें 'राधा' कहा गया है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 48.4671)
- **Original**: हैं। उनका चरणारविन्द ब्रह्मादि देवताओंके लिये श्रीराधाके रोमकूपोंसे गोपियोंका समुदाय प्रकट
- **Translation**: 

---

### Verse 19 (Vaivtpuran 48.4672)
- **Original**: परम दुर्लभ होनेपर भी भक्तजनोंके लिये सदा हुआ है तथा श्रोकृष्णके रोमकूपोंसे सम्पूर्ण गोपॉंका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 48.4673)
- **Original**: सुलभ है। सुदामाके शापसे देवी श्रीराधाको प्रादुर्भाव हुआ है। श्रीराधाके वामांश-भागसे
- **Translation**: 

---

