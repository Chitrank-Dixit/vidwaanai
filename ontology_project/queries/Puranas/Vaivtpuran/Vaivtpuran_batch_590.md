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

### Verse 1 (Vaivtpuran 47.4634)
- **Original**: धर्म, देवेद्र, मुनीन्द्र, सिद्धेन्र तथा सिद्धपुड्रवोंको समस्त देवियोंके चरित्रका श्रवण किया। अब मैं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 47.4635)
- **Original**: भी उसका ज्ञान नहीं है। सुरेश्वरि! तुम मुझसे भी श्रीराधाका उत्तम आख्यान सुनना चाहती हूँ। बलवती हो; क्योंकि इस प्रसड्गको न सुनानेपर श्रुतिमें कण्वशाखाके भीतर श्रीराधाकौ प्रशंसा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 47.4636)
- **Original**: अपने प्राणोंका परित्याग कर देनेको उद्यत हो गयी संक्षेपसे की गयी है, उसे मैंने आपके मुखसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 47.4637)
- **Original**: थीं। अत: मैं इस गोपनीय विषयको भी तुमसे सुना है; अब व्यासद्वारा वर्णित श्रीराधाकी महत्ता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 47.4638)
- **Original**: कहता हूँ। दुर्गे! यह परम अद्भुत रहस्य है। मैं सुनाइये। पहले आगमाख्यानके प्रसड्भमें आपने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 47.4639)
- **Original**: इसका कुछ वर्णन करता हूँ, सुनो। श्रीराधाका मेरी इस प्रार्थनाकों स्वीकार किया था। ईश्वरकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 47.4640)
- **Original**: चरित्र अत्यन्त पुण्यदायक तथा दुर्लभ है। वाणी कभी मिथ्या नहीं हो सकती। अत: आप
- **Translation**: 

---

### Verse 8 (Vaivtpuran 47.4641)
- **Original**: एक समय रासेश्वरी श्रीराधाजी श्यामसुन्दर श्रीराधाके प्रादुर्भाव, ध्यान, उत्तम नाम-माहात्म्य,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 47.4642)
- **Original**: श्रीकृष्णसे मिलनेको उत्सुक हुईं। उस समय वे उत्तम पूजा-विधान, चरित्र, स्तोत्र, उत्तम कवच, । रल्रमय सिंहासनपर अमूल्य रत्राभरणोंसे विभूषित आराधन-विधि तथा अभीष्ट पूजा-पद्धतिका इस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 47.4643)
- **Original**: होकर बैठी थीं। अग्निशुद्ध दिव्य वस्त्र उनके समय वर्णन कीजिये। भक्तवत्सल! मैं आपको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 47.4644)
- **Original**: श्रीअज्ञोंकी, शोभा बढ़ा रहा था। उनकी मनोहर भक्त हूँ, अत: मुझे ये सब बातें अवश्य बताइये।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 47.4645)
- **Original**: अज्भकान्ति करोड़ों पूर्ण चन्द्रमाओंको लज्जित कर साथ ही, इस बातपर भी प्रकाश डालिये कि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 47.4646)
- **Original**: रही थी। उनकी प्रभा तपाये हुए सुवर्णके सदृश आपने आगमाख्यानसे पहले ही इस प्रसड्रका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 47.4647)
- **Original**: जान पड़ती थी। वे अपनी ही दीप्तिसे दमक रही वर्णन क्‍यों नहीं किया था? थीं। शुद्धस्वरूपा श्रीराधाके अधरपर मन्द मुसकान पार्वतीका उपर्युक्त बचन सुनकर भगवान्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 47.4648)
- **Original**: खेल रही थी। उनकी दन्तपंक्ति बड़ी ही सुन्दर पश्ममुख शिवने अपना मस्तक नीचा कर लिया।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 47.4649)
- **Original**: थी। उनका मुखारविन्द शरत्कालके प्रफुल्ल अपना सत्य भद्ग होनेके भयसे वे मौन हो कमलॉको शोभाको तिरस्कृत कर रहा था। 5 गये--चिन्तामें पड़ गये। उस समय उन्होंने अपने । मालती-सुमनोंकी मालासे मण्डित रमणीय केशपाश इष्टदेव करुणानिधान भगवान्‌ श्रीकृष्णका ध्यानद्वारा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 47.4650)
- **Original**: धारण करती थीं। उनके गलेकौ रत्रमयी माला
- **Translation**: 

---

### Verse 18 (Vaivtpuran 48.4651)
- **Original**: ग्रीष्प-ऋतुके सूर्यके समान दीप्तिमती थी। कण्ठमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 48.4652)
- **Original**: हुई हैं। देवी महालक्ष्मी चतुर्भुज विष्णुकी पत्नी हैं प्रकाशित शुभ मुक्ताहार गद्भाकी धवल धारके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 48.4653)
- **Original**: और वैकुण्ठधाममें वास करती हैं। राजाको समान शोभा पा रहा था। रसिकशेखर श्यामसुन्दर
- **Translation**: 

---

