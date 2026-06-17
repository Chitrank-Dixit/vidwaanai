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

### Verse 1 (Vaivtpuran 13.11242)
- **Original**: दबाये जाते हुए गरुड़को मुनिने रोषभरी दृष्टिसे हों सके, तब सहसा वहाँ पक्षिराज गरुड़ प्रकट
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11243)
- **Original**: देखा। मुनिकी उस दृष्टिसे गरुड़ काँप उठे और हो गये। मुने! गरुड़को आया देख नागगण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11244)
- **Original**: वह महामत्स्य उनकी चोंचसे छूटकर पानीमें गिर कालियके प्राणोंकी रक्षा करनेके लिये जबतक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11245)
- **Original**: पड़ा। गरुड़के डरसे वह मीन मुनिके पास ठहर सूर्योदय नहीं हुआ, तबतक पूरी शक्ति लगाकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11246)
- **Original**: गया-उनके शरणागत हो गया। जब गरुड़ पुनः उनके साथ युद्ध करते रहे। अन्तमें पक्षिराजके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11247)
- **Original**: उसे लेनेको उद्यत हुए, तब मुनीन्द्रने उनसे कहा। तेजसे उद्ठिग्र हो वे सब-के-सब भाग खड़े हुए
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11248)
- **Original**: सौभरि बोले--पक्षिराज! मेरे पाससे दूर और सबके अभवदाता भगवान्‌ अनन्तकी शरणपमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11249)
- **Original**: हटो, दूर हटो। मेरे सामनेसे इस विशाल जीवको गये। नागोंकों भागते देख करुणानिधान कालिय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11250)
- **Original**: पकड़ लेनेकी तुममें क्‍या योग्यता है? तुम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11251)
- **Original**: + श्रीकृष्णजन्मखण्ड « 501 अं ै3343444222%242%4%440 0
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11252)
- **Original**: 0024044440 अपनेको श्रीकृष्णका वाहन समझकर बहुत बड़ा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11253)
- **Original**: यों कहने लगे--'हम क्‍या करें? हमारे श्रीहरि मानते हो। श्रीकृष्ण तुम्हारे-जैसे करोड़ों वाहन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11254)
- **Original**: कहाँ चले गये? हैं नन्दनन्दन! हे प्राणोंसे भी रच लेनेकी शक्ति रखते हैं। मैं अपनी भौंहें टेढ़ी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11255)
- **Original**: बढ़कर प्रियतम श्रीकृष्ण! हे बन्धो! हमें दर्शन करनेमात्रसे तुम्हें शीत्र और अनायास ही भस्म
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11256)
- **Original**: दो। हमारे प्राण निकले जा रहे हैं। कर सकता हूँ। तुम परमेश्वके जाहन हो तो क्या
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11257)
- **Original**: _ इसी बीचमें कुछ बालक नन्‍्दरायजीके हुआ ? हम लोग तुम्हारे दास नहीं हैं। पक्षिरगाज!
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11258)
- **Original**: निकट जा पहुँचे। वे अत्यन्त चल्लल थे और यदि आजसे कभी भी मेरे इस कुण्डमें आओगे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11259)
- **Original**: शोकसे व्याकुल होकर रो रहे थे। उन्होंने शीघ्र तो मेरे शापसे तत्काल भस्म हो जाओगे। यह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11260)
- **Original**: ही यशोदाकों, उनके पास बैठे हुए बलरामकों ध्रुव सत्य है। तथा अन्यान्य गोपों और लाल कमलके समान मुनीन्द्रकी बात सुनकर पक्षिराज विचलित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11261)
- **Original**: नेत्रोंवाली गोपाज़्नाऑंको यह समाचार बताया। हो गये। वे श्रीकृष्णेक चरणोंका स्मरण करते-
- **Translation**: 

---

