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

### Verse 1 (Bhagwat_Geeta 10.939)
- **Original**: आयुधानामहं वज्ज॑ धेनूनामस्मि कामधुक्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 10.940)
- **Original**: प्रजनश्चास्मि कन्दर्प: सर्पाणामस्मि वासुकि:
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 10.941)
- **Original**: मैं शस्त्रोंमें वज् और गौओंमें कामधेनु हूँ। शास्त्रोक्त रीतिसे सन्तानकी उत्पत्तिका हेतु कामदेव हूँ और सर्पोमें सर्पणज वासुकि हूँ
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 10.942)
- **Original**: अनन्तश्लास्मि नागानां वरुणो यादसामहम्‌। पितृणामर्यमा चास्मि यम: संयमतामहम्‌
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 10.943)
- **Original**: में नागोंमें' शेषगाग और जलचरोंका अधिपति वरुण देवता हूँ और पितरोंमें अर्यमा नामक पितर तथा शासन करनेवालोंमें यमराज मैं हूँ
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 10.944)
- **Original**: प्रह्मादश्चास्मि दैत्यानां काल: कलयतामहम्‌। मृगाणां च मृगेन्द्रोडहं वैनतेयश्व पक्षिणाम्‌
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 10.945)
- **Original**: मैं दैत्योंमें प्रहाद और गणना करनेवालोंका समय'" हूँ तथा पशुओंमें मृगराज सिंह और पक्षियोंमें मैं गरुड़ हूँ
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 10.946)
- **Original**: 1. नाग और सर्प यह दो प्रकारकी सर्पोकी ही जाति हैं। 2. क्षण, घड़ी, दिन, पक्ष, मास आदिमें जो समय है, वह मैं हूँ।
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 10.947)
- **Original**: * अध्याय 10* 137 पवन: पवतामस्मि रामः शस्त्रभूतामहम्‌। झषाणां मकरश्लास्मि स्त्रोतसामस्मि जाह्नवी
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 10.948)
- **Original**: मैं पवित्र करनेवालोंमें वायु और शस्त्रधारियोंमें श्रीराम हूँ तथा मछलियोंमें मगर हूँ और नदियोंमें श्रीभागीरथी गंगाजी हूँ
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 10.949)
- **Original**: सर्गाणामादिरन्तश्च॒ मध्यं चैवाहमर्जुन। अध्यात्मविद्या विद्यानां वादः प्रवदतामहम्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 10.950)
- **Original**: हे अर्जुन! सृष्टियोंका आदि और अन्त तथा मध्य भी मैं ही हूँ। मैं विद्याओंमें अध्यात्मविद्या अर्थात्‌ ब्रह्मविद्या और परस्पर विवाद करनेवालोंका तत्त्व-निर्णयके लिये किया जानेवाला वाद हूँ
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 10.951)
- **Original**: अशक्षराणामकारोउसिम द्वन्द्ः सामासिकस्य च। अहमेवाक्षय: कालो धाताहं विश्वतोमुख:
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 10.952)
- **Original**: मैं अक्षरोंमें अकार हूँ और समासोंमें द्वन्द्द नामक समास हूँ। अक्षयकाल अर्थात्‌ कालका भी महाकाल तथा सब ओर मुखवाला, विराट्स्वरूप, सबका धारण-पोषण करनेवाला भी मैं ही हूँ
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 10.953)
- **Original**: मृत्यु: सर्वहरश्राहमुद्धवश्च भविष्यताम्‌ । कीर्ति: श्रीर्वाक्च नारीणां स्मृतिर्मेधा धृति: क्षमा
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 10.954)
- **Original**: मैं सबका नाश करनेवाला मृत्यु और उत्पन्न
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 10.955)
- **Original**: 138 * श्रीमद्धगवद्रीता * होनेवालोंका उत्पत्ति हेतु हूँ तथा स्त्रियोंमें कीर्ति', श्री, वाकू, स्मृति, मेधा, धृति और क्षमा हूँ
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 10.956)
- **Original**: बृहत्साम तथा साम्नां गायत्री छन्‍्दसामहम्‌ । मासानां मार्गशीर्षो उहमृतूनां कुसुमाकरः
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 10.957)
- **Original**: तथा गायन करनेयोग्य श्रुतियोंमें मैं बृहत्साम और इछनन्‍्दोंमें गायत्री छन्द हूँ तथा महीनोंमें मार्गशीर्ष और ऋतुओंमें वसन्‍्त मैं हूँ
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 10.958)
- **Original**: झूतं॑ छलयतामस्मि तेजस्तेजस्विनामहम्‌ । जयोउस्मि व्यवसायोड5स्मि सत्त्वं सत््ववतामहम्‌।
- **Translation**: 

---

