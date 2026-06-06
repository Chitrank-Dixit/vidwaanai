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

### Verse 1 (Vaivtpuran 23.1882)
- **Original**: सिद्धिरूपा, सिद्धिदा, सिद्धिदाताओंकी ईश्वरी, पुरुष। उनका आधा दाहिना अड्गभ 'पुरुष' और [ बुद्धि, निद्रा, क्षुधा, पिपासा, छाया, तन्द्रा, दया, आधा बायाँ अड्ग 'प्रकृति' हुआ। वही प्रकृति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1883)
- **Original**: स्मृति, जाति, क्षान्ति भ्रान्ति, शान्ति, कान्ति, ब्रह्मस्वरूपा, नित्या और सनातनी माया है। जैसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1884)
- **Original**: चेतना, तुष्टि, पुष्टि, लक्ष्मी, वृत्ति और माता-ये परमात्मा हैं, वैसी उनकी शक्तिस्वरूपा प्रकृति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1885)
- **Original**: सब इनके नाम हैं। श्रीकृष्ण परब्रह्म परमात्मा है अर्थात्‌ परब्रह्म परमात्माके सभी अनुरूप गुण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1886)
- **Original**: हैं। उनके समीप सर्वशक्तिरूपसे ये बिराजतो हैं। इन प्रकृतिमें निहित हैं, जैसे अग्रिमें दाहिका शक्ति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1887)
- **Original**: श्रुतिमें इनके सुविख्यात गुणका अत्यन्त संक्षेपमें सदा रहती है। इसीसे परम योगी पुरुष स्त्री और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1888)
- **Original**: वर्णन किया गया है, जैसा कि आगमोंमें उपलब्ध पुरुषमें भेद नहीं मानते हैं। नारद! वे सबको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1889)
- **Original**: होता है। ये अनन्ता हैं। अतएव इनमें गुण भी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1890)
- **Original**: <6 * संक्षिप्त ब्रह्मवैवर्तपुराण « 666#44664#56444£664£66/446 6//654664&/64£/&/8 66 #4&6%4 55664 558 86 # 5 % 55% 8 % 55 # 5 $ अनन्त हैं। अब इनके दूसरे रूपका वर्णन करता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1891)
- **Original**: उनकी आराधना और बन्दना करते हैं। हूँ, सुनो। । नारद! अब मैं अन्य प्रकृतिदेवीका परिचय जो परम शुद्ध सत्त्वस्वरूपा हैं, उन्हें 'भगवती
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1892)
- **Original**: देता हूँ, सुनो। परब्रह्म परमात्मासे सम्बन्ध लक्ष्मी' कहा जाता है। परम प्रभु श्रीहरिकी वे रखनेवाली वाणी, बुद्धि, विद्या और ज्ञानकी जो शक्ति कहलाती हैं। अखिल जगत्‌की सारी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1893)
- **Original**: अधिष्ठात्री देवी. हैं, उन्हें 'सरस्वती' कहा जाता सम्पत्तियाँ उनके स्वरूप हैं। उन्हें सम्पत्तिकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1894)
- **Original**: है। सम्पूर्ण विद्याएँ उन्हींके स्वरूप हैं। मनुष्योंको अधिष्ठात्री देवी माना जाता है। वे परम सुन्दरी,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1895)
- **Original**: बुद्धि, कविता, मेधा, प्रतिभा और स्मरण-शक्ति अनुपम संयमरूपा, शान्तस्वरूपा, श्रेष्ठ स्वभावसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1896)
- **Original**: उन्हींकी कृपासे प्राप्त होती हैं। अनेक प्रकारके सम्पन्न तथा समस्त मड़ुलोंकों प्रतिमा हैं। लोभ,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1897)
- **Original**: सिद्धान्तभेदों और अर्थोंकी कल्पनाशक्ति वे ही मोह, काम, क्रोध, मद और अहंकार आदि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1898)
- **Original**: देती हैं। वे व्याख्या और बोधस्वरूपा हैं। उनकी दुर्गुणोंसे वे सहज ही रहित हैं। भक्तोंपर अनुग्रह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1899)
- **Original**: कृपासे समस्त संदेह नष्ट हो जाते हैं। उन्हें करना तथा अपने स्वामी श्रीहरिसे प्रेम करना
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1900)
- **Original**: विचारकारिणी और ग्रन्थकारिणी कहा जाता है। उनका स्वभाव है। वे सबकी आदिकारणरूपा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1901)
- **Original**: वे शक्तिस्वरूपा हैं। सम्पूर्ण संगीतकी सन्धि और और पतिव्रता हैं। श्रीहरि प्राणके समान जानकर
- **Translation**: 

---

