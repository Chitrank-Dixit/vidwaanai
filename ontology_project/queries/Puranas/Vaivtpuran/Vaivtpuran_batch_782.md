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

### Verse 1 (Vaivtpuran 543.13954)
- **Original**: उसको भस्म कर दिया। तत्पश्चात्‌ मन्त्रसे उस शत्रुका संहार कर डालूँगी। जिसे मैं मार दूँगी,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13955)
- **Original**: अभिमन्त्रित एक मुट्ठी धूल लेकर उसके द्वारा उसकी रक्षा कौन कर सकता है? मेरे बड़े भाई
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13956)
- **Original**: उन्होंने उस भस्मको भी निष्फल कर दिया। फिर और गुरु भगवान्‌ शेषने मुझे जगदी श्वर नारायणका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13957)
- **Original**: वे अवहेलनापूर्वक हँसने लगे। तब मनसादेवीने परम अद्भुत सिद्ध मन्त्र प्रदान किया है। मैं अपने ग्रीष्मकालके सूर्यकी भाँति प्रकाशित होनेवाली कण्ठमें “त्रैलोक्य-मज्जल' नामक उत्तम कबच
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13958)
- **Original**: शक्ति हाथमें ले ली और उसे मन्त्रसे आवेष्टित धारण करती हूँ; अत: संसारको भस्म करके पुनः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13959)
- **Original**: करके शत्रुकी ओर चला दिया। उस जाज्वल्यमान उसकी सृष्टि करनेमें समर्थ हूँ। मन्त्रशास्त्रॉंमें मैं
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13960)
- **Original**: शक्तिको आते देख धन्वन्तरिने भगवान्‌ विष्णुके भगवान्‌ शंकरकी शिष्या हूँ। पूर्वकालमें भगवान्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13961)
- **Original**: दिये हुए शूलसे अनायास ही उसके टुकड़े-टुकड़े शिवने कृपापूर्वक मुझे महान्‌ ज्ञान दिया था। । कर डाले। शक्तिको भी व्यर्थ हुई देख देवी मनसा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13962)
- **Original**: 606 * संक्षिप्त ब्रह्मवैवर्तपुराण * £745455%% 4 #5# 44% #% 4; # 4 46 # 6 $# 4 ;### #/## ## 5 $5 4 ## # ## # कई कक 4 4 4 अ# # 4 # # रोषसे जल उठी। अब उसने कभी व्यर्थ न
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13963)
- **Original**: विद्वान्‌ महाभाग धन्वन्तरे! मनसादेवीके साथ जानेवाले दुःसह एवं भयंकर नागपाशको हाथ्में
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13964)
- **Original**: तुम्हारा युद्ध हो, यह मुझे उचित नहीं जान पड़ता। लिया, जो एक लाख नागोंसे युक्त, सिद्धमन्त्रसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13965)
- **Original**: इसके साथ तुम्हारी कोई समता ही नहीं है। अभिमन्त्रित तथा काल और अन्तकके समान
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13966)
- **Original**: यह देवेश्वरी मनसा शिवके दिये हुए अमोघ तेजस्वी था। उसने क्रोधपूर्वक उस नागपाशको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13967)
- **Original**: शूलसे तीनों लोकोंकों जलाकर भस्म करनेकी चलाया। नागपाशको देखकर धन्वन्तरि प्रसन्नतासे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13968)
- **Original**: शक्ति रखती है। कौथुम-शाखामें वर्णित ध्यानके मुस्करा उठे; उन्होंने तत्काल गरुड़का स्मरण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13969)
- **Original**: अनुसार मनसादेवीका भक्तिभावसे ध्यान करके किया और पक्षिराज गरुड़ वहाँ आ पहुँचे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13970)
- **Original**: एकाग्रचित्त हो षोडशोपचार अर्पित करते हुए नागास्त्रको आया देख दीर्घकालके भूखे हुए
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13971)
- **Original**: इसको पूजा करो। फिर आस्तीकमुनिद्वारा किये हरिवाहन गरुड़ने चोंचसे मार-मारकर सब
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13972)
- **Original**: गये स्तोत्रसे तुम्हें इसकी स्तुति करनी चाहिये। नागोंकों अपना आहार बना लिया। प्रिये! इससे संतुष्ट हो मनसादेवी तुम्हें वर प्रदान करेगी। नागास्त्रको निष्फल हुआ देख मनसाके नेत्र रोपसे। .. ब्रह्माजीकी यह बात सुनकर शिवजीने भी लाल हो उठे। उसने एक मुट्ठी भस्म उठाया,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13973)
- **Original**: उसका अनुमोदन किया। फिर गरुड़ने प्रेमसे जिसे पूर्वकालमें भगवान्‌ शिवने दिया था। मन्त्रसे
- **Translation**: 

---

