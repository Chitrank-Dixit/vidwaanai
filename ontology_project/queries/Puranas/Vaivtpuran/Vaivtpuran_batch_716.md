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

### Verse 1 (Vaivtpuran 543.12634)
- **Original**: कृत्य किया। मुनिवर देवल मेरे भक्त एवं वहीं षोडशाक्षर मन्त्र, स्तोत्र, पूजाविधि, परम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12635)
- **Original**: जितेन्द्रिय थे। उन्होंने एक सहस््र दिव्य वर्षोतक अद्भुत 'संसार-विजय' नामक कवच तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12636)
- **Original**: गन्धमादनको गुफामें तप किया। पुरक्षणणका उपदेश दिया। साथ ही यह भी कहा एक दिन रम्भाने उन परम सुन्दर, शान्तस्वभाव कि 'इस मन्त्रकी इश्टदेवी तुम्हें वर देनेके लिये एवं कन्दर्पसदुश रूपवान्‌ मुनिको देख उनसे प्रत्यक्ष दर्शन देंगी।' यों कहकर रुद्रदेव चुप हो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12637)
- **Original**: मिलनकी प्रार्थना कौ। मुनिने उसकी याचना गये और असितमुनि उन्हें नमस्कार करके चले
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12638)
- **Original**: स्वीकार न करके कहा--'रम्भे! सुनो। मैं वेदोंका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12639)
- **Original**: 554 * संक्षिप्त ब्रह्मवैवर्तपुराण + सारभूत वचन सुना रहा हूँ, जो तपस्वी ब्राह्मणोंक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12640)
- **Original**: तैयार करके शोकवश अपने प्राण त्याग देनेको कुलधर्मके अनुकूल और सत्य है। जो मनुष्य
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12641)
- **Original**: उद्यत हुए। उस समय मैंने उन्हें दर्शन एवं वर अपनी पत्नीको त्यागकर परायी स्त्रीके साथ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12642)
- **Original**: दिया तथा दिव्य ज्ञान देकर उन्हें समझाया। सम्बन्ध स्थापित करता है, वह जीते-जी मरा प्रेमपूर्वक मेरे आश्वासन देनेपर वे शान्त हुए। हुआ है। उसके यश, धन और आयुकी हानि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12643)
- **Original**: उन महामुनिके आठों अज्ञोंको वक्र देख मैंने होती है। भूतलपर जिसके यशका विस्तार नहीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12644)
- **Original**: तत्काल ही कौतूहलवश उनका नाम अष्टावक्रा हुआ, उसका जीवन निष्फल है। एक तपस्वीको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12645)
- **Original**: रख दिया। मेरे कहनेसे उन्होंने मलयाचलकी उत्तम सम्पत्ति, राज्य और सुखसे क्या लेना है?
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12646)
- **Original**: कन्दरामें आकर साठ हजार वर्षोतक बड़ी भारी मैं निष्काम और वृद्ध हूँ। मुझसे तुम्हारा क्या
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12647)
- **Original**: तपस्या कौ। प्रिये! उस तपकी समाप्ति होनेपर प्रयोजन सिद्ध होगा? माँ! तुम सुन्दरी हो; अत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12648)
- **Original**: मेरा वह भक्त मुझसे आ मिला है। मैंने स्वयं किसी उत्तम वेशभूषावाले सुन्दर तरुण पुरुषकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12649)
- **Original**: उसे अपनेमें मिला लिया है। प्रलयकालमें सबके खोज करो।' नष्ट हो जानेपर भी मेरे भक्तका नाश नहीं होता। देवलजीकी यह बात सुनते ही रम्भाको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12650)
- **Original**: इस मुनिने आहार बिलकुल छोड़ दिया था। अतः क्रोध आ गया। उसने पुनः अपनी वहीं बात
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12651)
- **Original**: दीर्घकालकी तपस्या एवं जठराग्रिकी ज्वालासे दोहरायी। तब मुनि उसे कुछ भी उत्तर न देकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12652)
- **Original**: इनके शरीरका भीतरी भाग जलकर भस्मरूप हो पूर्ववत्‌ ध्यानस्थ हो गये। यह देख र्भाने गया था। प्रिये! ये मुनि मेरे ही लिये मलयाचलकी रोषपूर्वक शाप देते हुए कहा--'कुटिलह्ृदय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12653)
- **Original**: कन्दरा छोड़कर यहाँ आये थे। इन अष्टावक्र ब्राह्मण! तेरे सारे अवयब टेढ़े-मेढ़े हो जायें।
- **Translation**: 

---

