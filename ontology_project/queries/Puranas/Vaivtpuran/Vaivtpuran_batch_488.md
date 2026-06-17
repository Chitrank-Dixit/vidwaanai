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

### Verse 1 (Vaivtpuran 27.18836)
- **Original**: ब्रह्मानन्तेश शेषेद्ध धर्मादीनाप्रधीश्वर । सर्व सर्वेश शर्वेश बीजरूप नमोउस्तु ते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 27.18837)
- **Original**: प्रकृते प्राकृत प्राज्ञ प्रकृतीश परात्यर । संसारवृक्ष तदबीज फलरूप नमोउस्तु ते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 27.18838)
- **Original**: सृष्टिस्थित्यनतबीजेश . सृष्टिस्थित्यन्तकारण । महाविराद्‌_ तरोबीज राधिकेश नपोउस्तु ते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 27.18839)
- **Original**: अहो यस्थ त्रयः स्कन्धा ब्रह्मविष्णुमहेश्वराः। शाखा प्रशाखा बेदाद्यास्तपाँसि कुसुमानि च
- **Translation**: 

---

### Verse 5 (Vaivtpuran 27.18840)
- **Original**: संसारविफला एव प्रकृत्यड्भुरमेव च । तदाधार निराधार सर्वाधार नमोउस्तु ते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 27.18841)
- **Original**: तेजोरूप निराकार प्रत्यक्षानृरमेव अर । सर्वाकारातिप्रत्यक्ष स्वेच्छामय नमो5स्तु ते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 27.18842)
- **Original**: इति त्ीब्रह्मवैवर्ते अद्टावक्रकृत॑ श्रीकृष्णस्तोजं सम्पूर्णम्‌ ( श्रीकृष्णजन्मखण्ड 29। 40--48 ) 7<8<>रीप्पशएए9000000 श्रीकृष्णं द्रष्टमुत्सुकेनाक्ररेण तदीयमहिम्नो गानम्‌ अक्रूर उवाच सुप्रभाताद्य रजनी बभूब में शुभ दिनम्‌ । तुष्टाश्न गुरवों त्रिप्रा देवा मामिति निश्चितम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 27.18843)
- **Original**: कोटिजन्मार्जितं पुण्यं मम स्वयमुपस्थितम्‌ । बभूव मे समुत्पत्नं यद्‌ यत्कर्म शुभाशुभम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 27.18844)
- **Original**: चिच्छेद बन्धनिगडंं मम बद्धस्यथ कर्मणा । कारागाराश्च संसारान्मुक्तो यामि हरे: पदम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 27.18845)
- **Original**: सुहृदर्थी कृतोईह॑च्॒ कंसेन विदुषा रुघा । वरेण तुल्यो देवस्यथ क्रोधों मम बभूब ह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 27.18846)
- **Original**: ब्रजराज॑ समाहतु ब्रज यास्यामि साम्प्रतम्‌ । द्रक्ष्याम परम पूज्य भुक्तिमुक्तिप्रदायिनम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4177)
- **Original**: 186 + संक्षिप्त श्रह्मवैल्॑र्तपुराण + औ244204//।//4(4/20](2।]/82 8 54884 0 850 00870]20:49 5) 62040 52082 ]0624(6545]!]6 5] प्राणियोंका अन्त करते हैं, उन भगवान्‌ कृतान्तको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4178)
- **Original**: प्रसिद्ध भगवान्‌ धर्मराजको मैं प्रणाम करती हूँ। मैं प्रणाम करती हूँ। जो पापीजनोंको शुद्ध करनेके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4179)
- **Original**: जिनका जन्म ब्रह्माजीके बंशमें हुआ है तथा जो निमित्त दण्डनीयके लिये ही हाथमें दण्ड धारण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4180)
- **Original**: ब्रह्मतेजसे सदा प्रज्वलित रहते हैं एवं जिनके करते हैं तथा जो समस्त कर्मोंके उपदेशक हैं,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4181)
- **Original**: द्वारा परन्रह्मका सतत ध्यान होता रहता है, उन उन भगवान्‌ दण्डधरकों मेरा प्रणाम है। जो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4182)
- **Original**: ब्रह्मवंशी भगवान्‌ धर्मराजको मेरा प्रणाम है।* विश्वके सम्पूर्ण प्राणियोंका तथा उनकी समूची
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4183)
- **Original**: मुने! इस प्रकार प्रार्थना करके सावित्रीने आयुका निरन्तर परिगणन करते रहते हैं, जिनकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4184)
- **Original**: धर्मराजको प्रणाम किया। तब धर्मराजने सावित्रीको गतिको रोक देना अत्यन्त कठिन है, उन भगवान्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4185)
- **Original**: विष्णु-भजन तथा कर्मके विपाकका प्रसड्भ सुनाया। कालको मैं प्रणाम करती हूँ। जो तपस्वी, वैष्णव,
- **Translation**: 

---

