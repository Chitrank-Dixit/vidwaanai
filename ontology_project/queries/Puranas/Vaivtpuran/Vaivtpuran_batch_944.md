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

### Verse 1 (Vaivtpuran 543.17194)
- **Original**: रहता है। ज्ञानका उद्गीरण करने अर्थात्‌ उगलनेके तो स्वयं ब्रह्मस्वरूपा और श्रीकृष्णके वक्ष:-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17195)
- **Original**: कारण गुरु कहा जाता है; बह ज्ञान मन्त्र-तन्त्रसे स्थलपर वास करनेवाली हो। ब्रह्मा, शिव और ! प्राप्त होता है; बह मन्त्र और वह तन्त्र तुम दोनोंकी शेष आदि देवगण, सनकादि मुनिवर, जीवन्मुक्त भक्ति है। जब जीव प्रत्येक जन्ममें देवोंके मनत्रका भक्त और कपिल आदि सिद्धशिरोमणि, जिनके सेवन करता है तो उसे दुर्गके परम दुर्लभ अनुपम एवं परम दुर्लभ चरणकमलका निरन्तर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17196)
- **Original**: चरणकमलमें भक्ति प्राप्त हो जाती है। जब वह ध्यान करते हैं, उन श्रीकृष्णके प्राणोंकी तुम
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17197)
- **Original**: लोकोंके कारणस्वरूप शबम्भुके मन्त्रका आश्रय अधिदेवी तथा उनके लिये प्राणोंसे भी बढ़कर ग्रहण करता है, तब तुम दोनों (राधा- परम प्रियतमा हो। श्रीकृष्णके । माधव
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17198)
- **Original**: कृष्ण)-के अत्यन्त दुर्लभ चरणकमलको प्राप्त कर है और बामाड्से राधा प्रादुर्भूत हुई हैं। जगज्जननी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17199)
- **Original**: लेता है। जिस पुण्यवान्‌ पुरुषको तुम दोनोंके महालक्ष्मी तुम्हारे वामाड्रसे प्रकट हुई हैं। तुम
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17200)
- **Original**: दुष्प्राप चरणकमलकोी प्राप्ति हो जाती है, वह सबके निवासभूत वसुको जन्म देनेवाली, परमेश्वरी,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17201)
- **Original**: दैववश क्षणार्ध अथवा उसके षोड़शांश कालके बेदों और लोकॉंकी ईश्वरी मूलप्रकृति हो।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17202)
- **Original**: लिये भी उसका त्याग नहीं करता। जो मानव मात: ! इस सृष्टिमें जितनी प्राकृतिक नारियाँ हैं;
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17203)
- **Original**: इस पुण्यक्षेत्र भारतमें किसी वैष्णवसे तुम दोनोंके वे सभी तुप्हारी विभूतियाँ हैं। सारे विश्व कार्यरूप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17204)
- **Original**: मन्त्र, स्तोत्र अथवा कर्ममूलका उच्छेद करनेवाले हैं और तुम उनकी कारणरूपा हो। प्रलयकालमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17205)
- **Original**: कवचकों ग्रहण करके परमभक्तिके साथ उसका जब ब्रह्माका तिरोभाव हो जाता है; वह श्रीहरिका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17206)
- **Original**: जप करता है; वह अपने साथ-साथ अपनी एक निमेष कहलाता है। उस समय जो बुद्धिमान्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17207)
- **Original**: सहस्नों पीढ़ियोंका उद्धार कर देता है। जो मनुष्य योगी पहले राधा, फिर परात्पर कृष्ण अर्थात्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17208)
- **Original**: विधिपूर्वक वस्त्र, अलंकार और चन्दनद्वारा गुरुका राधा-कृष्णका सम्यक्‌ उच्चारण करता है; वह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17209)
- **Original**: भलीभाँति पूजन करके तुम्हारे कबचको धारण अनायास ही गोलोकमें चला जाता है। इससे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17210)
- **Original**: करता है, वह निश्चय ही विष्णु-तुल्य हो जाता व्यतिक्रम करनेपर वह महापापी निश्चय ही
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17211)
- **Original**: है। मात:! तुमने जो कुछ वस्तु मुझे समर्पित ब्रह्महत्याके पापका भागी होता है। तुम लोकोंकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17212)
- **Original**: की है, उस सबको सार्थक कर डालो अर्थात्‌ माता और परमात्मा श्रीहरि पिता हैं; परंतु माता
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17213)
- **Original**: अब मेरी प्रसन्नताके लिये उसे ब्राह्मणको दे दो। पितासे भी बढ़कर श्रेष्ठ, पूज्य, वन्दनीय और
- **Translation**: 

---

