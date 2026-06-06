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

### Verse 1 (Sama Ved 0.2201)
- **Original**: है शोधक अम्निदेव ! देवों के लिए हवि प्रदान करने वाले यजमान आपकी प्रार्थना त्परते हैं । आप उन्हें सुखी बनाएँ
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2202)
- **Original**: 847.मित्र॑ हुवे पृतदक्षं वरुणं च रिशादसम्‌। धियं घृताचीं साधन्ता
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2203)
- **Original**: जल उत्पादक मित्र और वरुणदेवों का हम आवाहन करते हैं । मित्रदेव हमें बलशाली बनाएँ, 0 था लाए हिंसक शत्रुओं का नाश करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2204)
- **Original**: उत्तराचिके चतुर्थोंध्याय: 4.3 848.ऋेन मित्रावरुणावृतावृधावृतस्पृशा । क्रतुं बृहन्तमाशाथे
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2205)
- **Original**: सत्य को फलितार्थ करने वाले, सत्य यज्ञ के पृष्टिकारक देव मित्रावरुणो ! आप दोनों हमारे पुण्यदायी कार्यों को सत्व से परिपूर्ण करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2206)
- **Original**: <49.कवी नो मित्रावरुणा तुविजाता उरुक्षया। दक्ष दधाते अपसम्‌
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2207)
- **Original**: अनेक कर्मों को सम्पन्न कराने वाले, विवेकशील, अनेक स्थलों में निवास करने वाले भित्रावरुणदव हमारी क्षमताओं और कार्यों को पुष्ट बनाते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2208)
- **Original**: 850,इन्द्रेण सं हि दृक्षसे संजग्मानो अविभ्युषा
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2209)
- **Original**: मन्दू समानवर्चसा
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2210)
- **Original**: सदा प्रसन्‍ रहने वाले, तेजस्वी, मरूदगण, निर्भय रहने वाले पराक्रमी इन्रदेव के साथ (संगठित हुए) अच्छे लगते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2211)
- **Original**: [ विभिल वर्णों के सपान प्रतिधा-सब्पन व्यवित परपर सहयोग करें, जो समाज सुखी होता है ।] 851.आदह स्वधामनु पुनर्गर्भत्वमेरिरे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2212)
- **Original**: दधाना नाम यज्ञियम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2213)
- **Original**: वे पूज्य, नाम धारण करने में समर्थ मरुत, शीघ्र हो अन्नादि (पोषक पदार्थों) को लक्ष्य करके, पुनः गर्भ को प्राप्त करके (उपयुक्त आकार) ग्रहण करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2214)
- **Original**: [ यह सूकत प्रकृति के चक्र को स्पष्ट करता है । पदार्थ उपयोग के बाद विखण्डित होकर (सड़-गलकर) वायुरूप हो जाता है। जीघ्र ही प्रकृति चक्र पें घूषकर पुन अनादि के रूप में प्रकट हो जाता है ।] 852.वीडु चिदारुजलुभिर्गुह्ा चिदिन्द्र वह्निभि: । अविन्द उम्निया अनु
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2215)
- **Original**: हे इन्धदेव ! सुदृढ़ किलेबंदी को ध्वस्त करने में समर्थ, तेजस्वी मरुद्गणों ने अवरुद्ध किरणों को प्रकट किया
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2216)
- **Original**: 853.ता हुवे ययोरिदं पप्ने विश्व॑ पुरा कृतम्‌। इन्द्राग्नी न भर्धतः
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2217)
- **Original**: सनातन, पराक्रमी, शत्रुनाशक, स्तोताओं के कष्टों को दूर करने वाले, इन्द्र और अग्निदेवों का हम आवाहन करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2218)
- **Original**: 854.उग्रा विघनिना मृथ इन्द्राग्नी हवामहे
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2219)
- **Original**: ता नो मृडात ईदृशे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2220)
- **Original**: शत्रुनाशक, महाबली, इन्द्र और अग्निदेबों का संग्राम (जीवन-समर) में सहायता के लिए हम आवाहन करते हैं, ये हमें सुखी बनायें
- **Translation**: 

---

