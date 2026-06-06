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

### Verse 1 (Vaivtpuran 15.6733)
- **Original**: लेनेवाली अत्यन्त सुन्दरी थी, जिसे विद्वान्‌ लोग बने हुए बहुत-से आभूषण, अग्निमें तपाकर शुद्ध
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6734)
- **Original**: शिशुओंकी रक्षा करनेवाली महाषष्ठी कहते हैं, किये हुए दो दिव्य वस्त्र, क्षीरसागरसे उत्पन्न हुई
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6735)
- **Original**: वैवाहिक विधिके अनुसार बेद-मन्त्रोच्चारणपूर्वक कौस्तुभमाण और वनमाला दो। त्रह्माने यज्ञसूत्र,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6736)
- **Original**: कार्तिकेयके अर्पित कर दिया। इस प्रकार वेद, बेदमाता गायत्री, संध्या-मन्त्र, कृष्ण-मन्त्र,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6737)
- **Original**: कुमारका अभिषेक करके सभी देवता, मुनिगण श्रीहरिका स्तोत्र और कवच, कमण्डलु, ब्रह्मास्त्र
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6738)
- **Original**: और गन्धर्व जगदीश्वरोंको प्रणाम करके अपने- तथा शत्रुविनाशिनी विद्या प्रदान की। धर्मने दिव्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6739)
- **Original**: अपने घर चले गये। धर्मबुद्धि और समस्त जीवोंपर दया समर्पित की।।._ नारद! इसके बाद शंकरने नारायण, ब्रह्मा शिबने परमोत्कृष्ट मृत्युक्ञय-ज्ञान, सम्पूर्ण शास्त्रोंका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6740)
- **Original**: और धर्मकी स्तुति को और फिर धर्मका ज्ञान, निरन्तर सुख प्रदान करनेवाला परम मनोहर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6741)
- **Original**: आलिज्ञन करके परमप्रिय श्रीहरिको मस्तक तत्त्वज्ञान, योगतत्त्व, सिद्धितत््व, परम दुर्लभ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6742)
- **Original**: झुकाया। “तदनन्तर शंकरद्वारा सत्कृत होकर ब्रह्मज्ञान, त्रिशूल, पिनाक, फरसा, शक्ति, पाशुपतास्त्र,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6743)
- **Original**: शैलराज हिमालय गणोंसहित प्रेमपूर्वक वहाँसे धनुष और संधान-संहारके ज्ञानसहित संहारास्त्र
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6744)
- **Original**: बिदा हुए। इस प्रकार जो-जो लोग वहाँ आये अर्पित किया। वरुणने श्वेत छत्र और रल्नोंकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6745)
- **Original**: थे, वे सभी आनन्दपूर्वक प्रस्थान कर गये। तब माला, महेद्धने गजराज, अमृतसागरने अमृतका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6746)
- **Original**: महेश्वर देवी पार्वतीके साथ बड़े आनन्दसे वहाँ कलश, सूर्यने मनके समान वेगशाली रथ और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6747)
- **Original**: रहने लगे। कुछ समय बीतनेके बाद शंकरने पुनः मनोहर कवच, यमने दमदण्ड और अग्रिने बहुत
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6748)
- **Original**: उन सभी देवॉंको बुलाकर विवाह-विधिके बड़ी शक्ति प्रदान की। इसी प्रकार अन्यान्य सभी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6749)
- **Original**: अनुसार पुष्टिको महात्मा गणेशके हाथों समर्पित देवताओंने भी हर्षपूर्वक नाना प्रकारके शस्त्र उन्हें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6750)
- **Original**: कर दिया। इस प्रकार दोनों पुत्रों तथा गणोंके भ्रंट किये। कामदेवने हर्षमग्र होकर उन्हें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6751)
- **Original**: साथ रहती हुई पार्वतीका मन बड़ा प्रसन्न था।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6752)
- **Original**: वे सम्पूर्ण कामनाओंके देनेवाले स्वामीके
- **Translation**: 

---

