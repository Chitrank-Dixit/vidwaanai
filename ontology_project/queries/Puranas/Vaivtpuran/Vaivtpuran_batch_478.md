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

### Verse 1 (Vaivtpuran 24.7129)
- **Original**: और ब्रह्मा अपने-अपने भवनकों चले गये। इस क्षणभरतक दसों दिशाओंको प्रकाशित करके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 24.7130)
- **Original**: प्रकार इसका वर्णन तो कर दिया, अब आगे स्वयं अन्तर्धान हो गया। फिर मुनिने रणके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 24.7131)
- **Original**: तुमसे कुछ और कहूँगा। (अध्याय 25-26) #1#-#7+/0 कल ल#222950.0050050 जमदग्रि-कार्तवीर्य-युद्ध, कार्तवीर्यद्वारा दत्तात्रेयदत्त शक्तिके प्रहारसे जमदग्रिका वध, रेणुकाका बिलाप, परशुरामका आना और क्षत्रियवधकी प्रतिज्ञा करना, भुगुका आकर उन्हें सान्त्वना देना नारायण कहते हैं--नारद! राजा घर लौट
- **Translation**: 

---

### Verse 4 (Vaivtpuran 24.7132)
- **Original**: आश्रमपर जाकर आश्रमको घेर लिया। राजाकी तो गया पर उसके मनमें युद्धकी लगी रही; इससे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 24.7133)
- **Original**: विशाल सेनाको देखकर जमदग्निके आश्रमवासी उसने लाखों सेना संग्रह करके फिर जमदग्निके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 24.7134)
- **Original**: भयसे मूर्च्छित हो गये। महर्षिने मन्त्रोच्चारणपूर्वक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 24.7135)
- **Original**: 346 « संक्षिसत खरह्म॒वैचतंपुराण * 0 2 2 9.
- **Translation**: 

---

### Verse 8 (Vaivtpuran 24.7136)
- **Original**: ]] 20000 0]27])7):)7++]]7[]7[]4]00]
- **Translation**: 

---

### Verse 9 (Vaivtpuran 24.7137)
- **Original**: 6। बाणोंका एक ऐसा जाल बिछाया कि उससे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 24.7138)
- **Original**: प्रणाम किया और पिताकी अभ्त्येष्टि-क्रियाकी आश्रमभूमि पूरी ढक गयी। सारी सेना उसीमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 24.7139)
- **Original**: तैयारी की। सारी बातें सुनकर माताके युद्ध न आबद्ध हो गयी। तब राजाने रथसे उतरकर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 24.7140)
- **Original**: करनेका अनुरोध करनेपर भी भार्गव परशुरामने महर्षिको नमस्कार किया। महर्षिने उसे आशीर्वाद
- **Translation**: 

---

### Verse 13 (Vaivtpuran 24.7141)
- **Original**: इक्कीस बार पृथ्वीको क्षत्रियहीन करनेकी प्रतिज्ञा दिया। राजाने फिर आक्रमण किया। यों कई बार
- **Translation**: 

---

### Verse 14 (Vaivtpuran 24.7142)
- **Original**: कर ली और राजा कार्तवीयार्जुके वध करनेका राजा आक्रमण करता रहा, मूर्च्छित होता रहा, पर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 24.7143)
- **Original**: प्रण कर लिया। फिर विलाप करती हुई पति- क्षमाशील मुनिने उसका वध नहीं किया। बड़ा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 24.7144)
- **Original**: शोकपीड़िता माताकों समझाते हुए बोले! घोर युद्ध हुआ। अन्तमें राजा कार्तवीर्यने दत्तात्रेय । परशुरामने कहा--माता! जो पिताकी मुनिके द्वारा प्राप्त एक पुरुषका नाश करनेवाली
- **Translation**: 

---

### Verse 17 (Vaivtpuran 24.7145)
- **Original**: आज्ञा भड़ करनेवाले तथा पिताके हिंसकका वध अमोघ शक्तिका प्रयोग किया। वह भगवान्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 24.7146)
- **Original**: नहीं करता, वह महान मूर्ख है। उसे निश्चय विष्णुकी शक्ति थी। उसने मुनिके हृदयकों बींध
- **Translation**: 

---

### Verse 19 (Vaivtpuran 24.7147)
- **Original**: ही रौरब नरकमें जाना पड़ता है। आग लगानेवाला, डाला। मुनिने उसके आघातसे जीवनविसर्जन कर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 24.7148)
- **Original**: विष देनेवाला, हाथमें हथियार लेकर मारनेके दिया। शक्ति भगवान्‌ विष्णुके पास चली गयी।
- **Translation**: 

---

