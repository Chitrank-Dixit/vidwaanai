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

### Verse 1 (Vaivtpuran 55.5305)
- **Original**: सदा सब ओरसे रक्षा करे। राधा पूर्व-दिशामें मेरी भक्तिसम्प्राप्तौ विनियोग:। रक्षा करें। कृष्णप्रिया अग्निकोणमें मेरा पालन इस जगन्मड्भरल राधाकवचके प्रजापति ऋषि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.5306)
- **Original**: करें। रासेश्वरी दक्षिणदिशामें मेरी रक्षाका भार हैं, गायत्री छन्द है, स्वयं रासेश्वरी देवता हैं और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.5307)
- **Original**: सँभालें। गोपीश्वरी नैत्यकोणमें मेरा संरक्षण श्रीकृष्णभक्ति-प्राप्तिक लिये इसका विनियोग
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.5308)
- **Original**: करें। निर्गुणा पश्चिम तथा कृष्णपूजिता वायव्यकोणमें बताया गया है। मेरा पालन करें। मूलप्रकृति ईश्वरी उत्तरदिशामें जो अपना शिष्य और श्रीकृष्णभक्त ब्राह्मण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.5309)
- **Original**: निरन्तर मेरे संरक्षणमें लगी रहें। सर्वपूजिता हो, उसीके समक्ष इस कवचको प्रकाशित करे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.5310)
- **Original**: सर्वेश्वरी सदा ईशानकोणमें मेरी रक्षा करें। महाविष्णु- जो शठ तथा दूसरेका शिष्य हो, उसको इसका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.5311)
- **Original**: जननी जल, स्थल, आकाश, स्वप्न और जागरणमें उपदेश देनेसे मृत्युकी प्राप्ति होती है। प्रिये!
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.5312)
- **Original**: सदा सब ओरसे मेरा संरक्षण करें। राज्य दे दे, अपना मस्तक कटा दे; परंतु दुर्गे! यह परम उत्तम श्रीजगन्मड्रलकबच अनधिकारीको यह कवच न दे। मैंने गोलोकमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.5313)
- **Original**: मैंने तुमसे कहा है। यह गूढ़से भी परम गूढ़तर देखा था कि साक्षात्‌ परमात्मा श्रीकृष्णने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.5314)
- **Original**: तत््व है। इसका उपदेश हर एकको नहीं देना भक्तिभावसे अपने कण्ठमें इसको धारण किया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.5315)
- **Original**: चाहिये। मैंने तुम्हारे ख्रेहतश इसका वर्णन किया था। पूर्वकालमें ब्रह्मा और विष्णुने भी इसे अपने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.5316)
- **Original**: है। किसी अनधिकारीके सामने इसका प्रवचन नहीं गलेमें स्थान दिया था। करना चाहिये। जो वस्त्र, आभूषण और चन्दनसे * 3» राधायै स्वाहा।' यह मन्त्र कल्पवृक्षके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.5317)
- **Original**: गुरुकी विधिवत्‌ पूजा करके इस कवचकों कण्ठ समान मनोबाजञ्छित फल देनेवाला है और श्रीकृष्णने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.5318)
- **Original**: या दाहिनी बाँहमें धारण करता है, वह भगवान्‌ इसकी उपासना की है। यह मेरे मस्तककी रक्षा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.5319)
- **Original**: विष्णुके समान तेजस्वी हो जाता है। सौ लाख करे। “3 हीं श्रीं राधिकायै स्वाहा।' यह मन्त्र मेरे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.5320)
- **Original**: जप करनेपर यह कवच सिद्ध हो जाता है। यदि कपालकी तथा दोनों नेत्रों और कानोंकी सदा रक्षा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.5321)
- **Original**: किसीको यह कवच सिद्ध हो जाय तो वह करे। 3» रां हीं श्री राधिकायै स्वाहा।' यह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.5322)
- **Original**: आगसे जलता नहीँ है। दुर्गें! पूर्वकालमें इस मन्त्रराज सदा मेरे मस्तक और केशसमूहोंकी रक्षा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.5323)
- **Original**: कवचको धारण करनेसे ही राजा दुर्योधनने करे। ' 3 रा राधायै स्वाहा।' यह सर्वसिद्धिदायक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.5324)
- **Original**: जल और अग्रिका स्तम्भन करनेमें निश्चितरूपसे मन्त्र मेरे कपोल, नासिका और मुखको रक्षा करे।
- **Translation**: 

---

