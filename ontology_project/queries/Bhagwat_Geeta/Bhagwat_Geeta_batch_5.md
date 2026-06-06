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

### Verse 1 (Bhagwat_Geeta 1.81)
- **Original**: इसके पश्चात्‌ शंख और नगारे तथा ढोल, मृदंग और नरसिंघे आदि बाजे एक साथ ही बज उठे। उनका वह शब्द बड़ा भयंकर हुआ
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 1.82)
- **Original**: ततः शवेतैईयैर्युक्ते महति स्यन्दने स्थितौ। माधव: पाण्डवश्नैव दिव्यौ शट्ज्गौ प्रदध्मतु:
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 1.83)
- **Original**: इसके अनन्तर सफेद घोड़ोंसे युक्त उत्तम रथमें बैठे हुए श्रीकृष्ण महाराज और अर्जुनने भी अलौकिक शंख बजाये
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 1.84)
- **Original**: पाझ्जन्यं हषीकेशो देवदत्त धनद्जयः। पौण्डुं दध्मौ महाशड्ड/ंं भीमकर्मा वृकोदरः
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 1.85)
- **Original**: श्रीकृष्ण महाराजने पाश्चजन्यनामक, अर्जुनने देवदत्तनामक और भयानक कर्मवाले भीमसेनने पौण्ड़्नामक महाशंख बजाया
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 1.86)
- **Original**: अनन्तविजयं राजा कुन्तीपुत्रो युथिष्टिर: । नकुल: सहदेवश्च सुघोषमणिपुष्पकौ
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 1.87)
- **Original**: * अध्याय 1*% श्छ कुन्तीपुत्र राजा युधिष्ठटिने अनन्तविजयनामक और नकुल तथा सहदेवने सुधोष और मणिपुष्पकनामक शंख बजाये
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 1.88)
- **Original**: काश्यश्व परमेष्वास: शिखण्डी च महारथ: । धृष्टद्युस्नो विराटश्व सात्यकिश्लवापराजित:
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 1.89)
- **Original**: द्रपदो द्रौपदेयाश्च सर्वशः पृथिवीपते। सौभद्रश्च महाबाहुः शट्डान्दध्मु: पृथक्‌ पृथक्‌
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 1.90)
- **Original**: श्रेष्ठ धनुषवाले काशिराज और महारथी शिखण्डी एवं धृष्टद्युम्न तथा राजा विराट और अजेय सात्यकि, राजा द्रुपद एवं द्रौपदीके पाँचों पुत्र और बड़ी भुजावाले सुभद्रापुत्र अभिमन्यु--इन सभीने, हे राजन्‌! सब ओरसे अलग-अलग शंख बजाये
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 1.91)
- **Original**: स घोषो धार्तराष्ट्राणां हृदयानि व्यदारयत्‌। नभश्च पृथिवीं चैव तुमुलो व्यनुनादयन्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 1.92)
- **Original**: और उस भयानक शब्दने आकाश और पृथ्वीको भी गुँजाते हुए धार्तराष्ट्रोंके अर्थात्‌ आपके पक्षवालोंके हृदय विदीर्ण कर दिये
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 1.93)
- **Original**: अथ व्यवस्थितान्दृष्टा धार्तराष्ट्रान कपिध्वज: । प्रवृत्ते शस्त्रसम्पाते धनुरुद्यम्य पाण्डव:
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 1.94)
- **Original**: हषीकेशं तदा वाक्यमिदमाह महीपते।
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 1.95)
- **Original**: 18 * श्रीमद्धगवद़ीता * अर्जुन उवाच सेनयोरु भयोर्म ध्ये रथं स्थापय मे<च्युत
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 1.96)
- **Original**: हे राजन्‌! इसके बाद कपिध्वज अर्जुनने मोर्चा बाँधकर डटे हुए धृतराष्ट्र-सम्बन्धियोंको देखकर, उस शस्त्र चलनेकी तैयारीके समय धनुष उठाकर हृषीकेश श्रीकृष्ण महाराजसे यह वचन कहा-हे अच्युत ! मेरे रथको दोनों सेनाओंके बीचमें खड़ा कीजिये
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 1.97)
- **Original**: यावदेतान्रिरीक्षे5ह॑ योब्द्ुकामानवस्थितान्‌। कैर्मयमा सह योद्धव्यमस्मिनरणसमुद्यमे
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 1.98)
- **Original**: और जबतक कि मैं युद्धक्षेत्रमें डटे हुए युद्धके अभिलाषी इन विपक्षी योद्धाओंको भलीप्रकार देख लूँ कि इस युद्धरूप व्यापारमें मुझे किन-किनके साथ युद्ध करना योग्य है तबतक उसे खड़ा रखिये
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 1.99)
- **Original**: योत्स्यमानानवेक्षेड्ह॑ य एतेउत्र समागताः
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 1.100)
- **Original**: धार्तराष्ट्रस्य॒दुर्ब॒ुद्धेर्युद्धे प्रियचिकीर्षव:
- **Translation**: 

---

