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

### Verse 1 (Vaivtpuran 63.5600)
- **Original**: आठ नायिकाओंका यत्ञतः पूजन करे। उनके नाम मज्लमय माध्वीक मधुपर्कके रूपमें प्रस्तुत है। इस प्रकार हैं--उग्रचण्डा, प्रचण्डा, चण्डोग्रा, इसे प्रसन्नतापूर्वक स्वीकार करो। (गन्ध) देवि!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5601)
- **Original**: चण्डनायिका, अतिचण्डा, चामुण्डा, चण्डा और विभिन्न वृक्षोंके मूलका चूर्ण गन्ध द्रव्यसे युक्त हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5602)
- **Original**: चण्डबती। अष्टदटल कमलपर पूर्व आदि दिशाके परम पवित्र एवं मड्जलोपयोगी गन्धके रूपमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5603)
- **Original**: क्रमसे इनकी स्थापना करके पञ्चोपचारोंद्वारा पूजन समर्पित है। इसे ग्रहण करो। (अर्ध्य) चण्डिके!
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5604)
- **Original**: करे। दलोंके मध्यभागमें भैरबोंका पूजन करना पवित्र शह्लुपात्रमें स्थित स्वर्गड्जाका जल दूर्वा, पुष्प
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5605)
- **Original**: चाहिये। उनके नाम इस प्रकार हैं-महाभैरव, और अक्षतसे युक्त अर्ध्यके रूपमें अर्पित है। इसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5606)
- **Original**: संहारभैरव, असिताडुभैरव, रुरुभैरव, कालभैरव, स्वीकार करो। (पुष्प) जगदम्बिके! पारिजात-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5607)
- **Original**: क्रोधभैरव, ताप्रचूडभैरव तथा चन्द्रचूडभैरव। इन वृक्षसे उत्पन्न सुगन्धित श्रेष्ठ पुष्प और मालती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5608)
- **Original**: सबकी पूजा करके बीचकीौ कर्णिकामें नौ आदि फूलोंकी माला ग्रहण करो। (नैवेद्य) शिवे!
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5609)
- **Original**: शक्तियोंका पूजन करे। क्रम यह है कि कमलके दिव्य सिद्धान्न, आमान्न, पीठा, खीर आदि, लड्डू
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5610)
- **Original**: आठ दलोंमें आठ शक्तियोंकी और बीचकी और दूसरे-दूसरे मिष्टात्न तथा सामयिक फल
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5611)
- **Original**: कर्णिकामें नरवीं शक्तिकी स्थापना करें। इस तरह नैवेद्यके रूपमें प्रस्तुत हैं। इन्हें स्वीकार करो।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5612)
- **Original**: इन सबका भक्तिपूर्वक पूजन करना चाहिये। इन (आचमनीय ) गिरिराजनन्दिनि! मैंने भक्तिभावसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5613)
- **Original**: शक्तियोंके नाम यों हैं--ब्रह्माणी, वैष्णवी, रौद्री, आचमनीयके रूपमें कर्पूर आदिसे सुसंस्कृत एवं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5614)
- **Original**: माहेश्वरी, नारसिंही, वाराही, इन्द्राणी तथा कार्तिकी सुवासित शीतल जल अर्पित किया है। इसे ग्रहण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5615)
- **Original**: (कौमारी)
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5616)
- **Original**: इनके अतिरिक्त नबों प्रधाना शक्ति हैं करो। (ताम्बूल) देवि! सुपारी, पान और चूनाको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5617)
- **Original**: सर्वमड्गला, जो सर्वशक्तिस्वरूपा हैं। इन नौ एकत्र करके उसे कर्पूर आदिसे सुवासित किया
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5618)
- **Original**: शक्तियोंका पूजन करनेके पश्चात्‌ कलशमें देवताओंका है। वही यह समस्त भोगोंमें श्रेष्ठ रमणीय ताम्बूल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5619)
- **Original**: पूजन करे। शंकर, कार्तिकेय, सूर्य, चन्द्रमा, अग्रि, है। इसे स्वीकार करो। (रत्लमय भूषण) देवि!
- **Translation**: 

---

