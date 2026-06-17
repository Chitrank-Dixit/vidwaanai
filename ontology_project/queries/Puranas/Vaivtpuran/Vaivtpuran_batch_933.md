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

### Verse 1 (Vaivtpuran 543.16974)
- **Original**: कोई नहीं है। मैं ही वैकुण्ठमें महालक्ष्मी, यथार्थ मधुर वचन बोलीं। गोलोकमें स्वयं राधिका, शिवलोकमें शिवा और पार्वतीजीने कहा--बाण ! तुम्हारे पास जो-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16975)
- **Original**: ब्रह्मलोकमें सरस्वती हूँ। पूर्वकालमें मैं ही दैत्योंका जो उत्तम मणि, रत्न, मोती, माणिक्य और हीरे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16976)
- **Original**: संहार करके दक्षकन्या सती हुई, फिर वही मैं आदि हैं, उस सारे धनकों तथा रत्नाभरणोंसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16977)
- **Original**: आपकी निन्दाके कारण शरीरका त्याग करके विभूषित अपनी कन्या उषाको रल्ननिर्मित आभूषणोंसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16978)
- **Original**: शैलकन्या पार्वती बनी। रक्तबीजके युद्धमें मैंने हो विभूषित परम श्रेष्ठ अनिरुद्धको आगे करके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16979)
- **Original**: मूर्तिभिदसे कालीका रूप धारण किया था। मैं ही परमात्मा श्रीकृष्णको सौंप दो और इस प्रकार अपने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16980)
- **Original**: वेदमाता सावित्री, जनकनन्दिनी सीता और भारतभूमिपर राज्यको निष्कण्टक बना लो। भला, जिसके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16981)
- **Original**: द्वारकामें भीष्मक-पुत्री रुक्मिणी हूँ। इस समय निकल जानेपर इन्द्रियॉंसहित सभी प्राण विलीन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16982)
- **Original**: दैववश सुदामाके शापसे मैं वृषभानुकी कन्या हो जाते हैं, उस जीवका आत्माके साथ युद्ध
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16983)
- **Original**: होकर प्रकट हुई हूँ और पुण्यमय वृन्दावनमें कैसा? मैं ही शक्ति हूँ, ब्रह्मा मन हैं और स्वयं श्रीकृष्णकी धर्मपली हूँ। आप तो स्वयं सर्वज्ञ शिव ज्ञानस्वरूप हैं। शिवका त्याग करके देह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16984)
- **Original**: सनातन भगवान्‌ शिव हैं। भला, मैं आपको क्‍या तुरंत ही गिर जाता है और शबरूप हो जाता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16985)
- **Original**: समयोचित कर्तव्य बतला सकती हूँ। है। शिवजी ! भला, संग्राममें सुदर्शनचक्रके तेजके (अध्याय 118) 820>0यरियििद6-00+000> शिवजीका कन्या देनेके लिये बाणको समझाना, बाणका उसे अस्वीकार करना, बलिका आगमन और सत्कार, बलिका महादेवजीका चरणवन्दन करके श्रीभगवान्‌का स्तवन करना, श्रीभगवान्‌द्वारा बलिको बाणके न मारनेका आश्वासन श्रीनारायण कहते हैं--नारद! पार्वतीको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16986)
- **Original**: करके श्रीकृष्णको दे दे। यही समस्त कर्मोंमें बात सुनकर गणेश, कार्तिकेय, काली तथा स्वयं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16987)
- **Original**: सामझस्य, यशस्कर और शुभदायक है। तुम्हारा शिव उनकी प्रशंसा करने लगे। तदनन्तर जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16988)
- **Original**: यह सारा कथन वेदसम्मत है; परंतु बाण परात्परा, ज्योति:स्वरूपा, परमा, मूलप्रकृति और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16989)
- **Original**: हिरण्यकशिपुका वंशज है; अत: यदि वह कन्या ईश्वरी हैं; उन जगज्जननी पार्वतीसे भगवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16990)
- **Original**: दे देता है और भयभीत होकर युद्धसे पराड्मुख शम्भु बोले। हो जाता है तो यह तुम्हारे लिये ही अकोर्तिकर श्रीमहादेवजीने कहा--देवेशि! तुमने जो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16991)
- **Original**: है। इसलिये शिवे! रणशास्त्रविशारद बाण कवच यह कहा है कि परमात्माके साथ युद्ध करना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16992)
- **Original**: धारण करके आगे चले; तत्पश्चात्‌ हम लोग भी अयुक्त तथा उपहासास्पद है; अत: बाण अपनी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16993)
- **Original**: कवचसे सुसज्जित हो उसका अनुगमन करेंगे। कन्या उषाको स्वर्णनिर्मित आभूषणोंसे विभूषित
- **Translation**: 

---

