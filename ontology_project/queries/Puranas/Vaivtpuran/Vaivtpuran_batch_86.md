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

### Verse 1 (Vaivtpuran 6.19385)
- **Original**: इति अीब्रह्मवैवतें ब्रह्मविकृत ्रीराधाकृप्णस्तोत्र सम्पूर्णम्‌ । ( श्रीकृष्णजन्मखण्ड 6। 21-23) यद्‌ दृष्ट च॒ श्रुतौ ध्यानं प्रशस्यं भ्रुतिसुन्दरम्‌। तन्निबोथ_ महाभधाग. भ्रमभम्जननकारणम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.19386)
- **Original**: सरस्वती शुक्लवर्णाँ सस्मितां सुमनोहराम्‌ । कोटिचन्द्रप्रभाजुष्टपुष्टश्रीयुक्तविग्रहाम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.19387)
- **Original**: वहिशुद्धांशुकाधानां. वीणापुस्तकधारिणीम्‌ । रतसारेन्द्रनिर्माणवरभूषणभूषिताम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.19388)
- **Original**: सुपूजितां सुरगणैर््नह्मविष्णुशिवादिभि:। वन्दे भक्‍त्या वन्दितां तां मुनीन्रमनुमानवैः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.19389)
- **Original**: (प्रकृतिखण्ड 4
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.19390)
- **Original**: 45--48 ) 40 सरस्वतीमन्त्र: सर्वोपयुक्तो मूलश्च॒वैदिकाष्टाक्षर: पर:।येषां येनोपदेशों वा तेषां स मूल एव च। सरस्वतीचतुर्थ्न्तों बहढ्िजायात्तन एव. च
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.19391)
- **Original**: श्री ही सरस्वत्यै स्वाहा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.19392)
- **Original**: लक्ष्मीमायादिकश्चैव मन्त्रोडयं कल्पपादप:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.19393)
- **Original**: (प्रकृतिखण्ड 4। 51-52) ]
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.19394)
- **Original**: _सरस्वतीकवचस ] कवचस्यास्यविप्रेद्न ऋषिरेष प्रजापति: । स्वयं .च बृहतीच्छन्दों देवता शारदाम्बिका#
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.19395)
- **Original**: सर्व॑तत्त्वपरिज्ञाने सर्वार्थाधनेषु.. च। कवितासु चर सर्वासु विनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.19396)
- **Original**: 37 हीं सरस्वत्ये स्वाहा शिरो मे पातु सर्वतः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.19397)
- **Original**: श्री वाग्देवतायै स्वाहा भाल॑ मे सर्बदाबतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.19398)
- **Original**: 39 सरस्वत्ये स्वाहेति श्रोत्रं पातु निरन्तरम्‌ । 30 श्रीं ह्रीं भारत्यै स्वाहा नेत्रयुग्म॑ सदावतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.19399)
- **Original**: ऐंड्डीं बाग्वादिन्ये स्वाहा नासां मे सर्वतोउवतु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.19400)
- **Original**: हीं विद्याथिष्ठातृदेव्य॒े स्वाहा ओए्ठं सदावतु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.19401)
- **Original**: 3 श्रीं हीं ब्राह्मण स्वाहेति दन्तपड्र्ती: सदावतु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.19402)
- **Original**: ऐमित्येकाक्षो मनत्रों मम कण्ठ॑ सदावतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.19403)
- **Original**: 3» श्रीं ह्लीं पातु मे ग्रीवां स्कन्ध॑ मे श्रीं सदावतु । श्रीं विद्याथिष्ठातृदेव्ये॑ स्वाहा वक्ष: सदावतु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.19404)
- **Original**: 3» हड्डी विद्यास्वरूपायै स्वाहा मे पातु नाभिकाम्‌। 3» हीं ह्रीं बाण्यै स्वाहेति मप्र पृष्ठ सदावतु
- **Translation**: 

---

