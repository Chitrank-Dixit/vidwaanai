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

### Verse 1 (Vaivtpuran 265.5037)
- **Original**: उसके अनुसार यह सब कुछ बता दिया। अब
- **Translation**: 

---

### Verse 2 (Vaivtpuran 265.5038)
- **Original**: तुम और क्‍या सुनना चाहते हो? पतन हो जाता है। आदिसर्गमें जगदुरु श्रीकृष्णने सुयज्ञने पूछा--ब्रह्माजीकी आयु पूर्ण होनेपर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 265.5039)
- **Original**: प्रकृतिके भीतर वीर्यका आधान किया था। पवित्र समस्त लोकोंके संहारकारी कालाग्रिरुद्र, तमोगुण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 265.5040)
- **Original**: वृन्दावनके भीतर रासमें उनके वामांशसे प्रकट तथा सत्त्वगुण यदि मृत्युज्रय शिवमें बिलीन होते
- **Translation**: 

---

### Verse 5 (Vaivtpuran 265.5041)
- **Original**: हुई रासेश्वरी राधा ही परा प्रकृति हैं। उन्होंने हैं तथा यदि उस प्राकृत लयकी बेलामें शिव
- **Translation**: 

---

### Verse 6 (Vaivtpuran 265.5042)
- **Original**: ही गर्भ धारण किया। तदनन्तर समय आनेपर निर्गुण परमात्मा श्रीकृष्णमें लीन होते हैं तो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 265.5043)
- **Original**: राधाने गोलोकके रासमण्डलमें एक अण्डको जन्म आपके गुरु भगवान्‌ शिवका नाम श्रुतिमें मृत्युज्ञय
- **Translation**: 

---

### Verse 8 (Vaivtpuran 265.5044)
- **Original**: दिया। अपनी संततिको अण्डाकार देख उनके क्यों रखा गया? तथा जिनके रोमकूपोंमें असंख्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 265.5045)
- **Original**: हृदयमें बड़ी व्यथा हुई। वे कुषित हो उठों तथा ब्रह्माण्ड निवास करते हैं, उन महाविष्णुकी जननी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 265.5046)
- **Original**: उन्होंने उस अण्डेको वहाँसे नीचे विश्वगोलकमें यह मूलप्रकृति कैसे हुई? फेंक दिया। उसी अण्डसे सबके आधारभूत सुतपा बोले--नरेश्वर! ब्रह्माजीकी आयु
- **Translation**: 

---

### Verse 11 (Vaivtpuran 265.5047)
- **Original**: महाविराट्‌ (महाविष्णु)-की उत्पत्ति हुई। पूर्ण होनेपर ब्रह्मा आदि समस्त लोकोंका संहार
- **Translation**: 

---

### Verse 12 (Vaivtpuran 265.5048)
- **Original**: सुयज्ञने कहा--प्रभो! आज मेरा जन्म करनेवाली मृत्युकन्या जलबिम्बकी भाँति नष्ट हो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 265.5049)
- **Original**: सफल हो गया। जीवन सार्थक हो गया। मेरे जाती है। ऐसी कितनी ही मृत्युकन्याओं और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 265.5050)
- **Original**: लिये आपका शाप भक्तिका कारण होनेसे वरदान करोड़ों ब्रह्मेऑओंका लय हो जानेपर यथासमय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 265.5051)
- **Original**: बन गया। समस्त मड़लोंका भी मड्जनल करनेवाली भगवान्‌ शिव सत्त्वरूपधारी निर्गुण श्रीकृष्णमें लीन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 265.5052)
- **Original**: हरि-भक्ति परम दुर्लभ है। विप्रवर! बेदोंमें जो होते हैं। मेरे गुरु भगवान्‌ शिवने मृत्युकन्यापर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 265.5053)
- **Original**: पाँच प्रकारकी भक्ति बतायी गयी है, वह भी सदा ही विजय पायी है। परंतु मृत्युने कभी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 265.5054)
- **Original**: इसके समान नहीं है। महामुने! परमात्मा शिवको पराजित नहीं किया है। यह बात प्रत्येक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 265.5055)
- **Original**: श्रीकृष्णमें जिस प्रकार भी मेरी भक्ति सम्भव कल्पमें श्रुतियोंद्वारा सुनी गयी है। अत: भगवान्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 265.5056)
- **Original**: हो सके, वह उपाय कौजिये; क्योंकि वह सभीके शिवका मृत्युञ्रय नाम उचित ही है। नरेश्वर!
- **Translation**: 

---

