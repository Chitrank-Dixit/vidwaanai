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

### Verse 1 (Vaivtpuran 13.11222)
- **Original**: वहाँ निःशद्भूभावसे खड़ा रहा। उसने गरुड़की समस्त संदेहोंका निवारण करनेवाले उन महर्षिसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11223)
- **Original**: ओर देखा और श्रीहरिके चरणारविन्दोंका चिन्तन अपना संदेह इस प्रकार पूछा। करके गरुड़के साथ युद्ध आरम्भ कर दिया। एक नारदजी बोले--जगदगुरो! अपने पहलेके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11224)
- **Original**: मुद्दूर्ततक उन दोनोंमें अत्यन्त भयानक युद्ध हुआ। उत्तम भवनकों छोड़कर कालिय यमुनातटको क्यों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11225)
- **Original**: अन्तमें गरुड़के तेजसे नागराज कालियकों पराजित चला गया था? इसका रहस्य मुझे बताइये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11226)
- **Original**: होना पड़ा। फिर तो वह भागा और यमुनाजीके भगवान्‌ श्रीनारायणने कहा--नारद! सुनो।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11227)
- **Original**: उसी कुण्डमें चला गया, जहाँ सौभरिके शापसे मैं उस प्राचीन इतिहासका वर्णन कर रहा हूँ,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11228)
- **Original**: पक्षिराज गरुड़ नहीं जा सकते थे। गरुड़के भयसे जिसे मैंने सूर्यग्रहणके समय मलयाचलपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11229)
- **Original**: नाग वहीं रहने लगा। पीछेसे उसके परिवारके सुप्रभा नदीके पश्चिम किनारे श्रीकृष्ण-कथाके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11230)
- **Original**: लोग भी वहीं चले गये। प्रसड्में पिता धर्मके मुखसे सुना था। पुलहने नारदजीने पूछा-- भगवन्‌! गरुड़को सौभरिका धर्मसे अपना संदेह पूछा था, तब कृपानिधान
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11231)
- **Original**: शाप कैसे प्राप्त हुआ? परमेश्वरके वाहन होकर धर्मने मुनियोंकी सभामें इस आश्चर्यमय आख्यानको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11232)
- **Original**: भी गरुड़ उस हृदमें क्‍यों नहीं जा सकते थे? सुनाया था। नारद! वहीं मैंने इसे सुना था, अतः भगवान्‌ श्रीनारायण बोले--उस कुण्डमें कहता हूँ, सुनो। सौभरि मुनि एक सहस््र दिव्य वर्षोंतक तपस्या भगवान्‌ शेषकी आज्ञासे नागगण प्रतिवर्ष करके महासिद्ध हो श्रीकृष्णके चरणकमलोंका कार्तिककी पूर्णिमाको भयके कारण गरुड़देवकौ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11233)
- **Original**: ध्यान करते थे। उन ध्यानपरायण मुनिके समीप पूजा करते हैं। पुष्प, धूप, दीप, नैवेद्य और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11234)
- **Original**: पक्षिराज गरुड़ यमुनाजीके जलमें तथा किनारे विविध उपहार-सामग्री अर्पित करके प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11235)
- **Original**: भी अपने गणोंके साथ प्रसन्नतापूर्वक निःशड्ढ उनकी आराधना करते हैं। महातीर्थ पुष्करमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11236)
- **Original**: विचरा करते थे। बे अपनी उत्कृष्ट इच्छासे प्रेरित भक्तिपूर्वक भलीभाँति स्नान करके कालियने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11237)
- **Original**: हो बहुधा पूँछ (अथवा पंख) ऊपरको उठाकर अहंकारवश उक्त तिथिको गरुड़की पूजा नहीं मुनिके अगल-बगलमें उनकी सानन्द परिक्रमा की। नागोंद्वारा जो पूजाकी सामग्री एकत्र की गयी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11238)
- **Original**: करते हुए जाते-आते थे। एक दिन उन्होंने थी, उसे कालियनाग बलपूर्वक खानेको उद्यत हो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11239)
- **Original**: परिवारसहित विशालकाय मौनको देखा। देखते- गया। तब सभी नाग उस मदमत्त कालियको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11240)
- **Original**: ही-देखते गरुड़ने मुनीन्द्रके निकटसे ही उस रोकने तथा उसे नीतिकी बात बताने लगे। जब
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11241)
- **Original**: मीनको चोंचसे पकड़ लिया। मछलीको मुँहमें किसी तरह भी वे कालियको रोकनेमें समर्थ न
- **Translation**: 

---

