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

### Verse 1 (Vaivtpuran 21.3724)
- **Original**: मनुष्योंको राजाकी सम्पत्ति सुलभ हो सकती है। करनेवाले श्यामरंगके पाषाणको “लक्ष्मीजनार्दन'
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.3725)
- **Original**: चौदह चक्रोंसे सुशोभित तथा नवीन मेघके समान कौ संज्ञा दी जानी चाहिये। दो द्वार, चार चक्र
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.3726)
- **Original**: रंगवाले स्थूल पाषाणको भगवान्‌ “अनन्त' का और गायके खुरके चिहसे सुशोभित एवं वनमालाके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.3727)
- **Original**: विग्नरह मानना चाहिये। उसके पूजनसे धर्म, अर्थ, नित्यं यस्तुलसीतोयं भुड्के भकत्या च मानव:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.3728)
- **Original**: स॒ एव जोवन्पुक्तश्ष॒ गड्भाज़ञानफल॑ लभेत्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.3729)
- **Original**: नित्य यस्तुलसीं दत्वा पूजयेन्मां च मानव: । सक्षाश्रमेधज॑ पुण्य॑ लभते नात्र संशय:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.3730)
- **Original**: तुलसीं स्‍्वकरें कृत्वा देहे धृत्वा च मानव: । प्राणांस्त्थजति तोर्थेषु विष्णुलोके स गच्छति
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.3731)
- **Original**: तुलसीकाष्ठनिर्माणपालां. गृह्याति यो. नरः। पदे परदे5श्रमेधस्प लभते निश्चित फलम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.3732)
- **Original**: तुलसीं स्‍्वकरे धृत्वा स्वीकार यो न रक्षति । स याति कालसूत्र च यावच्चन्द्रदिवाकरौ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.3733)
- **Original**: करोति मिथ्या शपथ तुलस्या यो हि मानव: । स याति कुम्भीपांकं च यावदिद्धाक्षतुर्दश
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.3734)
- **Original**: तुलसीतोयकणिकां मृत्युकाले च यो लपभेत्‌ । रत्र्यान॑ समारुद्य वैकुण्ठं स॒ प्रयाति च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.3735)
- **Original**: पूर्णिपायाममायां. च द्वादर्श्या तैलाभ्यड्रे च मध्याहे निशि संध्ययो:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.3736)
- **Original**: हर 5 धन तुलसों ये विचिन्वन्ति ते हिन्दन्ति हरे: शिर:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.3737)
- **Original**: श्राद्धे श्नतो च दाने च॒ प्रतिध्ायां सुरार्चने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.3738)
- **Original**: शुर्द्ध च तुलसीपत्र॑ क्षालनादन्यकर्मणि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.3739)
- **Original**: (प्रकृतिखण्ड 21
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.3740)
- **Original**: 32-53)
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.3741)
- **Original**: काम और मोक्ष-ये चारों फल प्राप्त होते हैं। जिसकी आकृति चक्रके समान हो तथा जो दो चक्र, श्री और गो-खुरके चिहसे शोभा पाता हो, ऐसे नवीन मेघके समान वर्णवाले मध्यम श्रेणोंके पाषाणको भगवान्‌ “मधुसूदन' समझना चहिये। केवल एक चक्रवाला 'सुदर्शन' का, गुप्तचक्र- चिहृवाला “गदाधर' का तथा दो चक्र एवं अश्वके मुखकी आकृतिसे युक्त पाषाण भगवान्‌ 'हयग्रीव' का विग्रह कहा जाता है। साध्वि! जिसका मुख अत्यन्त विस्तृत हो, जिसपर दो चक्र चिह्नित हों करती हैं। ब्रह्महत्या आदि जितने पाप हैं, वे सब शालग्राम-शिलाकी पूजा करनेसे नष्ट हो जाते हैं। छल्नाकार शालग्राममें राज्य देनेकी तथा वर्तुलाकारमें प्रचुर सम्पत्ति देनेकी योग्यता है। शकटके आकारवाले शालग्रामसे दुःख तथा शूलके नोकके समान आकारवालेसे मृत्यु होनी निश्चित है। विकृत मुखवाले दरिद्रता, पिडुलवर्णवाले हानि, भग्रचक्रवाले व्याधि तथा फटे हुए शालग्राम निश्चितरूपसे मरणप्रद हैं। व्रत, दान, प्रतिष्ठा तथा श्राद्ध आदि सत्कार्य शालग्रामकी संनिधिमें करनेसे सर्वोत्तम तथा जो बड़ा विकट प्रतीत होता हो ऐसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.3742)
- **Original**: हो सकते हैं। जो अपने ऊपर शालग्राम-शिलाका पाषाणकों भगवान्‌ 'नरसिंह' की प्रतिमा समझनी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.3743)
- **Original**: जल छिड़कता है, वह सम्पूर्ण तीथोंमें जञाव कर चाहिये। वह मनुष्यकों तत्काल बैराग्य प्रदान
- **Translation**: 

---

